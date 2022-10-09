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
    ) -> Union[pd.Series[Any], pd.DataFrame]:
        if self.name != "ETHBTC":
            raise ValueError(
                f"Sorry only random data for {self.name} is possible at the moment"
            )

        periods = len(pd.date_range(start=start_date, end=end_date, freq="Min"))

        df = random_ohlcv(start_date, periods=periods)

        if freq != "Min":
            return df.resample(freq).apply(OHLCVT)

        return df

    def rsi_signal(
        self,
        start_date: Union[str, pd.Timestamp],
        end_date: Union[str, pd.Timestamp],
        price_col="close",
        freq="Min",
        rsi_bounds: tuple[float, float] = (30, 70),
        **kwargs,
    ) -> pd.Series:
        """Relative Strength Index (RSI)

        Parameters
        ----------
        start_date : Union[str, pd.Timestamp]
            start date
        end_date : Union[str, pd.Timestamp]
            end date
        price_col : str, optional
            can be 'open, 'high', 'low' or 'close', by default "close"
        freq : str, optional
            pandas DateOffset by default "Min"
        rsi_bounds : tuple[float, float], optional
            upper and lower bound for the calculation of frequency bound breach, by default (30, 70)

        Returns
        -------
        pd.Series
            rsi timeseries

        Raises
        ------
        ValueError
            if 'price_col' not valid
        """

        if price_col not in PRICE_COLS:
            raise ValueError(f"{price_col} not in {PRICE_COLS}")

        ohlcv_data = self._get_ohlcv_data(
            start_date,
            end_date,
            freq=freq,
        )

        prices = ohlcv_data[price_col]
        self.rsi = rsi(prices, **kwargs)

        # rsi volue correlatio
        self.rsi_volume_corr = self.rsi.corr(ohlcv_data["volume"])

        # rsi percentage above below bounds
        self.rsi_bounds = pd.DataFrame(
            index=["RSI percentage"],
            columns=[
                f"{'below ' if i==0 else 'above '}{x}" for i, x in enumerate(rsi_bounds)
            ],
        )
        self.rsi_bounds.loc[f"below {rsi_bounds[0]}"] = (
            self.rsi.dropna() < rsi_bounds[0]
        ).value_counts().get(True, 0) / len(self.rsi.dropna())
        self.rsi_bounds.loc[f"above {rsi_bounds[1]}"] = (
            self.rsi.dropna() > rsi_bounds[1]
        ).value_counts().get(True, 0) / len(self.rsi.dropna())

        return self.rsi

    def trade_frequency_by_hour(
        self,
        start_date: Union[str, pd.Timestamp],
        end_date: Union[str, pd.Timestamp],
    ) -> pd.DataFrame:
        """Resample the minutely trade numbers to hours

        This is mainly used for the histogram plot


        Parameters
        ----------
        start_date : Union[str, pd.Timestamp]
            start date
        end_date : Union[str, pd.Timestamp]
            end date

        Returns
        -------
        pd.Dataframe
            minutely number of trades resampled to hour
        """

        periods = len(pd.date_range(start=start_date, end=end_date, freq="Min"))
        df = (
            random_ohlcv(start_date, periods=periods)[["number_of_trades"]]
            .resample("H")
            .sum()
        )
        # df.groupby(df.index.hour).mean()
        df["hour"] = df.index.hour
        return df
