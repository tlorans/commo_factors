import polars as pl

data = pl.read_parquet("commodity_futures.parquet")


returns = (
    data
    .sort(["symbol", "date"])
    .group_by("symbol")
    .map_groups(
        lambda df: df.select([
            pl.col("date"),
            pl.col("symbol"),
            pl.col("adjusted_close").pct_change().alias("ret")
        ])
    )
    .filter(pl.col("ret").is_not_null())
)

print(returns.head())

returns.write_parquet("commodity_futures_returns.parquet")
