# Data Source

For V1, the project uses `yfinance` to download NVDA intraday OHLCV data.

## Selected Source

- Source: Yahoo Finance via `yfinance`
- Ticker: NVDA
- Interval: 5m
- Period: 60d

## Required Columns

- timestamp
- open
- high
- low
- close
- volume

## Limitations

- Intraday history is limited
- Data is not guaranteed to be complete
- Not suitable for real trading
- Used only for learning and V1 development