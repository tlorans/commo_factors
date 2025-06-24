import yfinance as yf
import polars as pl

# Define commodity futures tickers
tickers = {
    # Energy
    "WTI Crude Oil": "CL=F",
    "Brent Crude Oil": "BZ=F",
    "Gasoline RBOB": "RB=F",
    "Heating Oil": "HO=F",
    "Natural Gas": "NG=F",
    "Propane": "PG=F",  # approximate or rarely available
    # Gasoil is not available directly on Yahoo Finance

    # Grains & Oilseeds
    "Corn": "ZC=F",
    "Wheat": "ZW=F",
    "Soybeans": "ZS=F",
    "Soybean Meal": "ZM=F",
    "Soybean Oil": "ZL=F",
    "Oats": "ZO=F",
    # Canola is traded on ICE Canada, not reliably on Yahoo

    # Livestock
    "Live Cattle": "LE=F",
    "Feeder Cattle": "GF=F",
    "Lean Hogs": "HE=F",
    # Pork Belly: contract discontinued

    # Metals
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Copper": "HG=F",
    "Platinum": "PL=F",
    "Palladium": "PA=F",
    # LME metals (Aluminum, Zinc, Nickel, etc.) are not on Yahoo Finance

    # Softs
    "Coffee": "KC=F",
    "Cocoa": "CC=F",
    "Cotton": "CT=F",
    "Sugar": "SB=F",
    "Orange Juice": "OJ=F",
    "Lumber": "LB=F",
    # Rubber is TOCOM, not on Yahoo
    # Ethanol and Milk may not have reliable tickers on Yahoo

    # Others
    "Ethanol": "EH=F",  # may exist, but not always available
    "Skim Milk": "DA=F",  # Approximate dairy futures ticker
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
pl_df = pl_df.select(["date", "symbol", "volume", "open", "low", "high", "close", "adjusted_close"]
                     ).filter(pl.col("adjusted_close") > 0)

print(pl_df.head())

pl_df.write_parquet("commodity_futures.parquet")
