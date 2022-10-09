import pandas as pd
import numpy as np
from typing import Union
from pathlib import Path


def random_ohlcv(
    start_date: Union[str, pd.Timestamp],
    periods: int,
    freq: Union[str, pd.DateOffset],
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

    seed = np.random.RandomState(seed=seed)
    _id = pd.date_range(
        start=start_date,
        periods=periods,
        freq=freq,
    )
    df = pd.DataFrame({"close_time": _id + pd.Timedelta(59, "s")}, index=_id)
    df[["open", "close"]] = np.random.random((periods, 2))
    df[["low", "high"]] = np.sort(np.random.random((periods, 2)), axis=1)
    df["number_of_trades"] = np.random.randint(0, 200)
    df["volume"] = round(np.random.randint(0, 1000000) * 0.001, 2)
    df["quote_asset_volume"] = (
        df[["open", "high", "low", "close"]].mean(axis=1) * df["volume"]
    )

    return df


if __name__ == "__main__":
    random_ohlcv("2000", periods=12 * 5 * 30, freq="D")
