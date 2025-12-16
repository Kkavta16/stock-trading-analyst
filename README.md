# Stock Price Decision Engine

A simple Python tool that fetches stock data using Yahoo Finance and provides Buy/Sell/Hold recommendations based on a Moving Average Crossover strategy.

## Features

- **Fetch Historical Data**: Retrieves 2 years of history for any valid ticker.
- **Moving Averages**: Calculates 20-day and 50-day Simple Moving Averages (SMA).
- **Decision Engine**:
    - **BUY**: When 20-day SMA crosses *above* 50-day SMA (Golden Cross).
    - **SELL**: When 20-day SMA crosses *below* 50-day SMA (Death Cross).
    - **HOLD**: When the trend continues without a new crossover.

## Setup

1.  **Install Python**: Ensure you have Python installed.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script:

```bash
python fetch_stock.py
```

Enter a ticker symbol when prompted (e.g., `AAPL`, `MSFT`, `TSLA`). Type `q` to quit.

## Example Output

```text
Enter ticker symbol: AAPL

--- Analyzing AAPL ---
Fetching data for AAPL...
Current Price: $274.11
SMA 20: $276.38 (Prev: $276.30)
SMA 50: $268.05 (Prev: $267.72)
Decision for AAPL: HOLD (No new crossover, current: Uptrend)
```
