import yfinance as yf
import polars as pl

# Define commodity futures tickers
tickers = {
    "WTI Crude Oil": "CL=F",
    "Gold": "GC=F",
    "Corn": "ZC=F",
    "Wheat": "ZW=F",
    "Soybeans": "ZS=F",
    "Silver": "SI=F",
    "Copper": "HG=F",
    "Natural Gas": "NG=F",
    "Coffee": "KC=F",
    "Cotton": "CT=F"
}

# Download monthly data
df = yf.download(list(tickers.values()), start="2000-01-01", interval="1d", auto_adjust=False)
df = df.stack(level=1).reset_index()  # Convert from wide to long format

# Convert to Polars DataFrame
pl_df = pl.from_pandas(df)

# Rename columns to lowercase and consistent names
pl_df = pl_df.rename({
    "Date": "date",
    "Ticker": "symbol",
    "Adj Close": "adjusted_close",
    "Close": "close",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Volume": "volume"
})

# Reorder columns
pl_df = pl_df.select(["date", "symbol", "volume", "open", "low", "high", "close", "adjusted_close"])

print(pl_df.head())

pl_df.write_parquet("commodity_futures.parquet")
