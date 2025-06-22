from plotnine import *
import pandas as pd
import polars as pl


prices = (
    pl.read_parquet("commodity_futures.parquet").to_pandas()
)

from mizani.breaks import date_breaks
from mizani.formatters import date_format

prices_figure = (
  ggplot(prices, aes(y="adjusted_close", x="date", color="symbol"))
  + geom_line()
  + scale_x_datetime(date_breaks="5 years", date_labels="%Y")
  + labs(x="", y="", color="", title="Commodity Futures Prices")
  + theme(legend_position="none")
)
prices_figure.show()

prices_figure.save("../../docs/docs/images/priced_factors/commodity_futures_prices.png", dpi=300, width=10, height=6)