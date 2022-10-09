# import pytest
from rsidemo.stats import rsi
import numpy as np
import pandas as pd

rand = np.random.RandomState(1337)
ret = pd.Series(
    rand.randn(1, 120)[0] / 100.0,
    index=pd.date_range("2000-1-30", periods=120, freq="M"),
)


def test_rsi():
    print()
    rsi(ret * 100, ma_type="ema")
