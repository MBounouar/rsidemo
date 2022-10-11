# Based on the example from https://www.activestate.com/blog/dash-vs-bokeh/
import dash

from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from dash_bootstrap_components.themes import BOOTSTRAP
from components.layout import create_layout
import uvicorn as uvicorn
import pandas as pd
import numpy as np
from models import RsiSignalModel, InstrumentOHLCV
from pydantic.schema import schema
from typing import Union, Optional
import datetime
from data import random_ohlcv

OFFSETS = {"Min": pd.offsets.Minute(), "H": pd.offsets.Hour(), "D": pd.offsets.Day()}

dapp = dash.Dash(
    __name__,
    requests_pathname_prefix="/",
    external_stylesheets=[BOOTSTRAP],
    title="Demo",
)


dapp.layout = create_layout(dapp)


server = FastAPI(
    title="RSI Demo API",
    description="Basic API Demo",
)


@server.get("/home")
def index():
    return {"message": "Hello world!"}


@server.put("/trendsignal/rsi")
async def rsi_trend_signal(
    # model: RsiSignalModel = Depends(),
    model: RsiSignalModel,
) -> JSONResponse:
    print(model.dict())
    ts = pd.Series(
        np.random.random_sample(12) * 100,
        index=pd.date_range("2020", periods=12, freq="Min"),
    )

    return JSONResponse({"asdfasdfasdf": ts.to_json()})


@server.get("/ohlcv/{instrument}")
async def ohlcv_data(
    instrument: str,
    startDate: Union[str, datetime.datetime, datetime.date],
    endDate: Union[
        str, datetime.datetime, datetime.date
    ] = datetime.datetime.now().replace(second=0, microsecond=0),
    freq: str = "Min",
) -> JSONResponse:
    start_date = pd.Timestamp(startDate)
    if endDate == startDate:
        if freq == "Min":
            end_date = pd.Timestamp(startDate) + OFFSETS["H"]
        elif freq == "H":
            end_date = pd.Timestamp(startDate) + OFFSETS["H"]
        elif freq == "D":
            end_date = pd.Timestamp(startDate) + OFFSETS["D"]
    else:
        end_date = pd.Timestamp(endDate)

    periods = len(pd.date_range(start=start_date, end=end_date, freq="Min"))
    df = random_ohlcv(start_date, periods=periods, resample_freq=freq)
    return df.to_json(orient="records")


server.mount("/", WSGIMiddleware(dapp.server))

if __name__ == "__main__":
    uvicorn.run("main:server", port=8080, reload=True)
