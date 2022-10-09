import pandas as pd


def rsi(
    prices: pd.Series,
    window: int = 14,
    ma_type: str = "ema",
) -> pd.Series:
    """Relative Strenght Index (RSI)

    Parameters
    ----------
    prices : pd.Series
        prices
    window : int, optional
        window lenght, by default 14
    ma_type : str, optional
        type of moving average `sma` or `ema`, by default "sma"

    Returns
    -------
    pd.Series
        rsi values

    Raises
    ------
    ValueError
        when ma_type is not valid
    """
    close_delta = prices.diff()

    # Make two series: one for lower closes and one for higher closes
    positive = close_delta.clip(lower=0)
    negative = -close_delta.clip(upper=0)

    if ma_type.lower() == "ema":
        # Use exponential moving average
        ma_up = positive.ewm(com=window - 1, adjust=True, min_periods=window).mean()
        ma_down = negative.ewm(com=window - 1, adjust=True, min_periods=window).mean()

    elif ma_type.lower() == "sma":
        # Use simple moving average
        ma_up = positive.rolling(window=window).mean()
        ma_down = negative.rolling(window=window).mean()
    else:
        raise ValueError(f"ma_type `{ma_type}` not recognized, must be `sma` or `ema`")

    rsi = 100.0 - (100.0 / (1.0 + (ma_up / ma_down)))
    rsi.name = f"RSI: {prices.name} - {ma_type} - {window}"
    return rsi
