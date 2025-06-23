import os
from dotenv import load_dotenv
from commodities_api import CommoditiesApiClient
import pandas as pd
from plotnine import *
from datetime import datetime, timedelta

# Load API key
load_dotenv()
api_key = os.getenv("COMMODITIES_API_KEY")
client = CommoditiesApiClient(access_key=api_key)

# Parameters
base_currency = "USD"
start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2025-06-22", "%Y-%m-%d")
max_days = 30

symbols = {
    "spot": "LME-XCU",
    "futures": "XCU"
}

def get_price_series_loop(symbol: str, label: str) -> pd.DataFrame:
    all_chunks = []

    current_start = start_date
    while current_start <= end_date:
        current_end = min(current_start + timedelta(days=max_days - 1), end_date)

        response = client.get_time_series(
            start_date=current_start.strftime("%Y-%m-%d"),
            end_date=current_end.strftime("%Y-%m-%d"),
            base=base_currency,
            symbols=symbol
        )

        if not response.get("data", {}).get("success"):
            raise Exception(f"API error fetching {label} from {current_start} to {current_end}: {response}")

        rates = response["data"]["rates"]
        df = pd.DataFrame.from_dict(rates, orient="index")
        df.index = pd.to_datetime(df.index)
        df = 1 / df
        df = df.rename(columns={symbol: "price"})
        df["type"] = label
        df["date"] = df.index

        all_chunks.append(df[["date", "price", "type"]])

        current_start = current_end + timedelta(days=1)

    return pd.concat(all_chunks).sort_values("date")

# Fetch both time series
spot_df = get_price_series_loop(symbols["spot"], "Spot")
futures_df = get_price_series_loop(symbols["futures"], "Futures")

# Combine and plot
combined_df = pd.concat([spot_df, futures_df])

plot = (
    ggplot(combined_df, aes(x="date", y="price", color="type"))
    + geom_line()
    + labs(
        title="COAL Spot vs Futures Prices (6-Month Period)",
        x="Date",
        y="Price in USD",
        color="Type"
    )
)

plot.show()
