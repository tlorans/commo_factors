from plotnine import *
import pandas as pd
import polars as pl


soybean_price = (
    pl.read_parquet("commodity_futures.parquet").filter(pl.col("symbol") == "ZS=F").to_pandas()
)

soybean_prices_figure = (
    ggplot(soybean_price, aes(x="date", y="adjusted_close")) +
    geom_line(color="blue") +
    labs(title="Soybean Futures Prices", x="Date", y="Adjusted Close Price")
)

soybean_prices_figure.show()

soybean_prices_figure.save("../../docs/docs/images/priced_factors/soybean_futures_prices.png", dpi=300, width=10, height=6)
