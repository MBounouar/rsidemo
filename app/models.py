from typing import Union
import datetime
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from typing import List


class RsiSignalModel(BaseModel):
    startDate: int
    endDate: int
    priceCol: str = Field("close")
    freq: str = Field("Min")


class RsiSignal(BaseModel):
    dt: int
    value: float


class RsiSignals(BaseModel):
    data: List[RsiSignal]


class MinuteOHCLV(BaseModel):
    id: int
    open: str
    high: str
    low: str
    close: str
    volume: str
    close_time: int
    quote_asset_volume: str
    number_of_trades: str


class InstrumentOHLCV(MinuteOHCLV):
    name: str
    ohlcv: List[MinuteOHCLV]
