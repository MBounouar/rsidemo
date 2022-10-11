from dash import Dash, html, dcc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import datetime


def render(app: Dash) -> html.Div:
    return dcc.DatePickerRange(
        id="my-date-picker-range",
        month_format="D-M-Y",
        min_date_allowed=datetime.datetime(1995, 8, 5),
        max_date_allowed=datetime.datetime(2017, 9, 19),
        initial_visible_month=datetime.datetime(2017, 8, 5),
        # end_date=datetime.date(2017, 8, 25),
    )

    # html.Div(id="output-container-date-picker-range"),
    # ],
    # id="output-container-date-picker-range",
    # ),
    # )
