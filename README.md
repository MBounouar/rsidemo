[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/github/MBounouar/rsidemo/branch/main/graph/badge.svg?token=1H51ZECQ7H)](https://codecov.io/github/MBounouar/rsidemo)
[![CodeFactor](https://www.codefactor.io/repository/github/mbounouar/rsidemo/badge)](https://www.codefactor.io/repository/github/mbounouar/rsidemo)

# rsidemo

Basic Demo

## Installation

Ensure that you have the latest version of `python v3.9`, I encountered issues with the default install on some systems i.e. `v.3.9.5`.

Clone the repository:

`git clone git@github.com:MBounouar/rsidemo.git`

or

`git clone https://github.com/MBounouar/rsidemo.git`

Ideally use a virtual environement like `pipenv` or similar.

Don't forget to upgrade `pip install --upgrade pip` to at least version `21.3.1`

`pip install -e .`

## Usage example

```python
from rsidemo.asset import Instrument
from rsidemo.plotting import plot_average_trading_by_hour, plot_rsi

ethbtc = Instrument("ETHBTC")

data = ethbtc.rsi_signal(
    start_date="2018 Jan",
    end_date="2019 Jan",
    price_col="close",
    window=8,
    freq="D",
    rsi_bounds=(30, 70),
)

# percentage of times when the RSI is below 30 or above 70
print(ethbtc.rsi_bounds)

# correlation between the volume and the RSI value
print(ethcbtc.rsi_volume_corr)

fig1 = plot_rsi(data=data, title="ETH-BTC")
fig1.show()

df = ethbtc.trade_frequency_by_hour(start_date="2018 Jan", end_date="2018 Mar")
fig2 = plot_average_trading_by_hour(df)
fig2.show()
```

## Output

![RSI Plot](https://github.com/MBounouar/rsidemo/blob/main/docs/rsi_plot.png?raw=true "Rsi Plot")
![Trade Hist Plot](https://github.com/MBounouar/rsidemo/blob/main/docs/trade_histo.png?raw=true "Trade Hist Plot")
