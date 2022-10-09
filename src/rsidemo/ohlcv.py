import pandas as pd
from typing import Union
from .utils import get_utc_timestamp


class RsiSignal:
    def __init__(
        self,
        start_date: Union[str, pd.Timestamp],
        end_date: Union[str, pd.Timestamp],
        instrument: str,
    ) -> None:
        if start_date is not None:
            self.start_date = get_utc_timestamp(self.start_date)
        if end_date is not None:
            self.end_date = get_utc_timestamp(self.start_date)

        self.instrument = instrument

    # _id: int
    # open: float
    # high: float
    # low: float
    # close: float
    # close_time: float
    # quote_asset_volume: float
    # number_of_trades: float

    def _get_data_from_json(
        self,
    ) -> None:
        pass


{
    "_id": 1600204260000,
    "open": "0.03371800",
    "high": "0.03372700",
    "low": "0.03369200",
    "close": "0.03369500",
    "volume": "413.19300000",
    "close_time": 1600204319999,
    "quote_asset_volume": "13.93363240",
    "number_of_trades": 98,
}
