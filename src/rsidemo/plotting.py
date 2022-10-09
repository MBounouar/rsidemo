import plotly.graph_objects as go

# from plotly.subplots import make_subplots
import pandas as pd


def plot_rsi(data: pd.Series, title: str = "") -> go.Figure:
    """RSI plot

    Parameters
    ----------
    data : pd.Series
        Series with RSI data
    title : str, optional
        title, by default ""

    Returns
    -------
    go.Figure
        plotly figure object
    """  #
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            name=data.name,
            meta=data.name,
            x=data.index,
            y=data.values,
            mode="lines",
        ),
    )
    fig.add_trace(
        go.Scatter(
            x=[data.index[0], data.index[-1]],
            y=[70, 70],
            mode="lines",
            line_color="lightblue",
            line=dict(dash="4px"),
            hoverinfo="skip",
            showlegend=False,
        ),
    )

    fig.add_trace(
        go.Scatter(
            x=[data.index[0], data.index[-1]],
            y=[30, 30],
            mode="lines",
            line_color="orangered",
            line=dict(dash="4px"),
            hoverinfo="skip",
            showlegend=False,
        ),
    )
    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            y=0.9,
            xanchor="center",
            yanchor="top",
        ),
        yaxis=dict(
            title="RSI",
        ),
    )

    return fig


def plot_average_trading_by_hour(data: pd.DataFrame) -> go.Figure:
    """Average trading by hour plot

    Parameters
    ----------
    data : pd.DataFrame


    Returns
    -------
    go.Figure
        plotly Figure object
    """
    fig = go.Figure(
        go.Histogram(
            x=data["hour"].apply(lambda x: str(x) + "H"),
            y=data["number_of_trades"],
            histfunc="avg",
        )
    )

    fig.update_layout(
        # title=dict(
        #     text="Average Number of Trades",
        #     x=0.5,
        #     y=0.85,
        #     xanchor="center",
        #     yanchor="top",
        # ),
        # bargap=0.05,
        yaxis=dict(title="Average Number of Trades"),
        xaxis=dict(
            title="Time",
            # tickformat=",.1%",
            ticks="outside",
        ),
    )

    return fig
