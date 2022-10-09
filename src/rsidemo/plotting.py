import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


def plot_rsi(data: pd.DataFrame) -> go.Figure:
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data["open"],
            high=data["high"],
            low=data["low"],
            close=data["close"],
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=[df.index[0], data.index[-1]],
            y=[70, 70],
            mode="lines",
            line_color="lightblue",
            line=dict(dash="4px"),
        ),
        row=2,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=[df.index[0], data.index[-1]],
            y=[30, 30],
            mode="lines",
            line_color="orangered",
            line=dict(dash="4px"),
        ),
        row=2,
        col=1,
    )

    fig.update_layout(xaxis_rangeslider_visible=False)
    return fig


if "__main__" == __name__:
    from rsidemo.data import random_ohlcv

    df = random_ohlcv("2000", periods=12 * 5 * 30, freq="D")
    fig = plot_rsi(data=df)
    fig.show()
