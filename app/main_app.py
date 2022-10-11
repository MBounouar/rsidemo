from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import datetime
from fastapi.encoders import jsonable_encoder
from typing import List


class RsiSignalModel(BaseModel):
    startDate: int
    endDate: int
    priceCol: str = Field("close")
    freq: str = Field("Min")


class RsiSignal(BaseModel):
    _id: int
    rsi: float


class RsiSignals(BaseModel):
    data: List[RsiSignal]


class Item(BaseModel):
    title: str
    timestamp: datetime.datetime
    description: Union[str, None] = None


app = FastAPI(
    title="RSI Demo API",
    description="Basic API Demo",
)

TEST = [{"_id": 1234, "rsi": 50.0}, {"_id": 1235, "rsi": 30}]


@app.get("/")
async def root():
    return {"status": "ready"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/bla", response_model=RsiSignals)  # , response_model_exclude_unset=True)
async def read_signal():
    return RsiSignals(data=TEST)


@app.post("/signal/rsi/")
def trend_signal_rsi(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    print(item)
    print(json_compatible_item_data)
    return JSONResponse(content=json_compatible_item_data)


@app.post("/trendsignal/rsi")
async def rsi_trend_signal(
    model: RsiSignalModel,
    request: Request,
):
    return JSONResponse({"bla": 2})
