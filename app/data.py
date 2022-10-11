import pandas as pd
from typing import Union
from pathlib import Path
import datetime


OHLCVT = {
    "open": "first",
    "high": "max",
    "low": "min",
    "close": "last",
    "volume": "sum",
    "quote_asset_volume": "sum",
    "number_of_trades": "sum",
}


def random_ohlcv(
    start_date: Union[str, pd.Timestamp],
    periods: int,
    seed: int = 12345,
    resample_freq="Min",
) -> pd.DataFrame:
    """Returns random minute sample of OHLCV data

    Parameters
    ----------
    start_date : Union[str, pd.Timestamp]
        start date
    periods : int
        number of periods to return
    seed : int, optional
        random seed, by default 12345

    Returns
    -------
    pd.DataFrame
        OHLCV sampled data
    """
    df = pd.read_json(
        Path(__file__).parent / "data/ethbtc.json.tar.gz", compression="infer"
    )

    columns = [
        "_id",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_volume",
        "number_of_trades",
    ]
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
    df.index = pd.date_range(start=start_date, periods=periods, freq="Min")
    df.index.name = "_id"

    if resample_freq != "Min":
        df = df.resample(resample_freq).apply(OHLCVT)

    df.index = df.index.map(datetime.datetime.timestamp).map(int)
    df = df.reset_index()
    df["close_time"] = df["_id"] + 59

    return df[columns]
