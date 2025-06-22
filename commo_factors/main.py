def main():
    print("Hello from commo-factors!")
    import yfinance as yf
    import pandas as pd

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
    data = yf.download(list(tickers.values()), start="2000-01-01", interval="1mo", auto_adjust=False)

    # Extract adjusted close and rename columns
    monthly_prices = data['Adj Close']
    monthly_prices.columns = list(tickers.keys())

    # Display last 12 rows
    print(monthly_prices.tail(12))

    # Optionally save to CSV
    monthly_prices.to_csv("monthly_commodity_futures.csv")


if __name__ == "__main__":
    main()
