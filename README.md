[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/github/MBounouar/rsidemo/branch/main/graph/badge.svg?token=1H51ZECQ7H)](https://codecov.io/github/MBounouar/rsidemo)
[![CodeFactor](https://www.codefactor.io/repository/github/mbounouar/rsidemo/badge)](https://www.codefactor.io/repository/github/mbounouar/rsidemo)

# rsidemo

Basic Demo

## Installation

`git clone git@github.com:MBounouar/rsidemo.git`

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
    print(self.rsi_bounds)

    # correlation between the volume and the RSI value
    print(self.rsi_volume_corr)

    fig1 = plot_rsi(data=data, title="ETH-BTC")
    fig1.show()

    df = ethbtc.trade_frequency_by_hour(start_date="2018 Jan", end_date="2018 Mar")
    fig2 = plot_average_trading_by_hour(df)
    fig2.show()
```

## Output

![RSI Plot](https://github.com/MBounouar/rsidemo/blob/develop/docs/rsi_plot.png?raw=true "Rsi Plot")
![Trade Hist Plot](https://github.com/MBounouar/rsidemo/blob/develop/docs/trade_histo.png?raw=true "Trade Hist Plot")
