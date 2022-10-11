from dash import Dash, html
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as obj
from components import candlestick_chart, datepicker
import datetime


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        children=[
            html.H1(children="Demo"),
            datepicker.render(app),
            candlestick_chart.render(app),
        ]
    )
