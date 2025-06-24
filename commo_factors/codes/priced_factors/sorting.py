import pandas as pd
import numpy as np
import statsmodels.api as sm
from regtabletotext import prettify_result


LOW_Q, HIGH_Q = 0.01, 0.99        # 1-percent winsorisation tails

# ── 1. Load panel of excess returns ────────────────────────────────────
# expected columns: date (yyy-mm-dd), ticker, ret  (monthly excess return in decimal form)
raw = (
    pd.read_parquet("commodity_futures_returns.parquet")
    .query("date >= '2010-01-01'")  # filter for dates if needed
)


# 2. Winsorise returns cross-sectionally each month
def winsorise_month(df: pd.DataFrame) -> pd.DataFrame:
    """Clip ret to [1st, 99th] percentile for this month’s cross section."""
    lo = df["ret"].quantile(LOW_Q)
    hi = df["ret"].quantile(HIGH_Q)
    return df.assign(ret=df["ret"].clip(lower=lo, upper=hi))

wins = (
    raw
      .assign(date=lambda d: pd.to_datetime(d["date"]))
      .groupby("date")
      .apply(winsorise_month)
      .reset_index(drop=True)
)

# ── 2. Momentum: cumulative product of (1+ret) for the past 11 months ────────
# but we have in daily data, so we need to adjust the window
# to account for the number of trading days in a month (typically around 20-22
# trading days per month).
# Here we use a window of 11 months, which is approximately 220 trading days.
def add_momentum(df: pd.DataFrame, window: int = 220) -> pd.DataFrame:
    """
    Add a 'momentum' column: cumulative return from t-12 to t-2
    (skip the most-recent month, hence shift(1)).
    """
    # Ensure date column is datetime and properly sorted
    df = df.assign(date=pd.to_datetime(df["date"])).sort_values("date")
    
    # Rolling cumulative return = Π(1+ret) − 1
    df["momentum"] = (
        df["ret"]
        .shift(1)                                     # skip last month
        .rolling(window=window, min_periods=window)   # t-12 … t-2 (11 obs)
        .apply(lambda x: (1 + x).prod() - 1, raw=True)
    )
    return df

panel = (
    wins
    .groupby("symbol")  # keep original index
    .apply(add_momentum)
    .reset_index(drop=True)
    .dropna(subset=["momentum"])  # drop rows where momentum is NaN
)

panel["rebalance_date"] = panel["date"].dt.to_period("M").dt.to_timestamp()




# ── 4. Month-by-month portfolio formation ──────────────────────────────
#     and equal-weight (mean) portfolio returns
n_port = 3                                       # quintiles (change as desired)

rebalancing_universe = (
    panel
    .drop_duplicates(subset=["symbol", "rebalance_date"])  # one row per symbol per month
    .groupby("rebalance_date")
    .apply(lambda x: x.assign(
        portfolio=pd.qcut(x["momentum"], q=[0, 0.5, 1], labels=["low", "high"])
    ))
    .reset_index(drop=True)
    .dropna(subset=["portfolio"])
    .get(["symbol", "rebalance_date", "portfolio"])
)

# Merge daily panel with monthly portfolio assignment
panel_with_portfolio = (
    panel
    .merge(rebalancing_universe, on=["symbol", "rebalance_date"], how="left")
    .dropna(subset=["portfolio"])  # drop rows before first assignment
)


daily_portfolio_returns = (
    panel_with_portfolio
    .groupby(["date", "portfolio"], as_index=False)
    .agg(ret=("ret", "mean"))  # equal-weight return
)


print(daily_portfolio_returns.head())


# 2️⃣ compute cumulative return within each portfolio
cumulative_rets = (
    daily_portfolio_returns.sort_values(["portfolio", "date"])  # sort by portfolio and date
      .groupby("portfolio")          # one time-series per portfolio
      .apply(lambda df: df.assign(
          cumulative_ret=(1 + df["ret"]).cumprod() # running product minus 1
      ))
      .reset_index(drop=True)
)

cumulative_rets.to_csv("cumulative_momentum_portfolios.csv", index=False)

from plotnine import * 

# ── 5. Plotting the portfolio returns ───────────────────────────────────
plot = (
    ggplot(cumulative_rets, aes(x="date", y="cumulative_ret", color="portfolio")) +
    geom_line() +
    labs(title="Momentum Portfolio Returns",
         x="Date",
         y="Monthly Return",
         color="Portfolio")
)

plot.show()

plot.save("../../docs/docs/images/priced_factors/momentum_portfolios.png", dpi=300)

long_short = (daily_portfolio_returns
  .pivot_table(index="date", columns="portfolio", values="ret")
  .reset_index()
  .assign(long_short=lambda x: x["low"]-x["high"])
)



cum_long_short = (
    long_short
    .assign(cumulative_long_short=lambda x: (1 + x["long_short"]).cumprod() - 1)
)

# plot long short returns
plot_ls = (
    ggplot(cum_long_short, aes(x="date", y="cumulative_long_short")) +
    geom_line(color="blue") +
    labs(title="Cumulative Long-Short Momentum Returns",
         x="Date",
         y="Cumulative Return")
)

plot_ls.show()

plot_ls.save("../../docs/docs/images/priced_factors/momentum_long_short.png", dpi=300, width=10, height=6)

# ────────────────────────────────────────────────────────────────────────
# 1.  Equal-weight “market” portfolio (all contracts each day)  🚩
# ────────────────────────────────────────────────────────────────────────
market_daily = (
    wins                       # winsorised daily returns you already created
      .groupby("date", as_index=False)
      .agg(mkt_ret=("ret", "mean"))   # simple equal-weight
)

# cumulative market return
market_cum = (
    market_daily
      .assign(cumulative_mkt=lambda d: (1 + d["mkt_ret"]).cumprod() - 1)
      .get(["date", "cumulative_mkt"])
)


# ────────────────────────────────────────────────────────────────────────
# 2.  Combine long-short and market series for plotting  🚩
# ────────────────────────────────────────────────────────────────────────
plot_df = (
    cum_long_short[["date", "cumulative_long_short"]]
      .merge(market_cum, on="date", how="inner")
      .melt(id_vars="date", var_name="series", value_name="cum_ret")
      .replace({
          "cumulative_long_short": "Long-Short factor",
          "cumulative_mkt": "Commodity market"
      })
)

plot_both = (
    ggplot(plot_df, aes(x="date", y="cum_ret", color="series")) +
    geom_line() +
    labs(
        title="Cumulative Return: Momentum Long-Short vs. Commodity Market",
        x="Date", y="Cumulative Return",
        color=""
    )
)

plot_both.show()

plot_both.save("../../docs/docs/images/priced_factors/momentum_long_short_vs_market.png", dpi=300, width=10, height=6)

model_fit = (sm.OLS.from_formula(
    formula="long_short ~ 1",
    data=long_short
  )
  .fit(cov_type="HAC", cov_kwds={"maxlags": 6})
)
prettify_result(model_fit)