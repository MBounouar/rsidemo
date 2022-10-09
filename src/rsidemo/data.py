import pandas as pd
# import numpy as np
from typing import Union
from pathlib import Path


def random_ohlcv(
    start_date: Union[str, pd.Timestamp],
    periods: int,
    seed: int = 12345,
) -> pd.DataFrame:
    df = pd.read_json(
        Path(__file__).parent / "data/ethbtc.json.tar.gz", compression="infer"
    )
    # columns = {
    #     "open": "float",
    #     "high": "float",
    #     "low": "float",
    #     "close": "float",
    #     "volume": "float",
    #     "close_time": "datetime64[ns]",
    #     "quote_asset_volume": "float",
    #     "number_of_trades": "int64",
    # }

    # rseed = np.random.RandomState(seed=seed)
    df = df.sample(periods, replace=True, random_state=seed, ignore_index=True)
    df.index = pd.date_range(
        start=start_date,
        periods=periods,
        freq="Min",
    )
    # df["close_time"] = df.index + pd.Timedelta(59, "s")

    return df
