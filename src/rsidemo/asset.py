from dataclasses import dataclass
import pandas as pd

# from functools import lru_cache
from .stats import rsi
from typing import Union, Any
from .data import random_ohlcv

PRICE_COLS = ["open", "high", "low", "close"]

OHLCVT = {
    "open": "first",
    "high": "max",
    "low": "min",
    "close": "last",
    "volume": "sum",
    "quote_asset_volume": "sum",
    "number_of_trades": "sum",
}


@dataclass
class Instrument:
    """
    Instrument class using random OHLCV data.

    """

    name: str

    def _get_ohlcv_data(
        self,
        start_date: Union[str, pd.Timestamp],
        end_date: Union[str, pd.Timestamp],
        freq: str = "D",
    ) -> None:
        if self.name != "ETHBTC":
            raise ValueError(
                f"Sorry only random data for {self.name} is possible at the moment"
            )

        periods = len(pd.date_range(start=start_date, end=end_date, freq="Min"))

        df = random_ohlcv(start_date, periods=periods)

        if freq != "Min":
            self.ohlcv_data = df.resample(freq).apply(OHLCVT)

        self.ohlcv_data = df

    def rsi_signal(
        self,
        start_date,
        end_date,
        price_col="close",
        freq="Min",
        rsi_bounds=(30, 70),
        **kwargs,
    ) -> dict[str, Any]:

        if price_col not in PRICE_COLS:
            raise ValueError(f"{price_col} not in {PRICE_COLS}")

        self._get_ohlcv_data(
            start_date,
            end_date,
            freq=freq,
        )

        prices = self.ohlcv_data[price_col]
        self.rsi = rsi(prices, **kwargs)
        self.rsi_volume_corr = self.rsi.corr(self.ohlcv_data["volume"])
        self.rsi_bounds = pd.DataFrame(
            index=["RSI percentage"],
            columns=[
                f"{'below ' if i==0 else 'above '}{x}" for i, x in enumerate(rsi_bounds)
            ],
        )
        self.rsi_bounds.loc[f"below {rsi_bounds[0]}"] = (
            self.rsi < rsi_bounds[0]
        ).value_counts()[True] / len(self.rsi)
        self.rsi_bounds.loc[f"above {rsi_bounds[1]}"] = (
            self.rsi > rsi_bounds[1]
        ).value_counts()[True] / len(self.rsi)
        return self.rsi

    def trade_frequency_by_hour(self, start_date, end_date):
        periods = len(pd.date_range(start=start_date, end=end_date, freq="Min"))
        df = (
            random_ohlcv(start_date, periods=periods)[["number_of_trades"]]
            .resample("H")
            .sum()
        )
        # df.groupby(df.index.hour).mean()
        df["hour"] = df.index.hour
        return df
