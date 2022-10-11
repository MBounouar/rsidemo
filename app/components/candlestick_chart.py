from dash import Dash, html, dcc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import requests
import json
import pandas as pd
import datetime

URL = "http://localhost:8080"


def render(app: Dash) -> html.Div:
    @app.callback(
        Output("candlestick-chart", "children"),
        [Input("my-date-picker-range", "value")],
    )
    def update_candlestickchart(slider) -> html.Div:
        response = requests.get(
            f"{URL}/ohlcv/eth?startDate=2021-08-11T18%3A20%3A00&endDate=2021-10-11T18%3A31%3A00&freq=D"
            # verify=False,
        )
        x = json.loads(response.content.decode("utf8"))
        df = pd.json_normalize(json.loads(x))
        print(df)
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=df["_id"].apply(datetime.datetime.fromtimestamp),
                    open=df["open"],
                    high=df["high"],
                    low=df["low"],
                    close=df["close"],
                )
            ]
        )

        return html.Div(dcc.Graph(figure=fig), id="candlestick-chart")

    return html.Div(id="candlestick-chart")
