import yfinance as yf
import pandas as pd

def fetch_data(ticker_symbol, period="2y"):
    """
    Fetches historical stock data from Yahoo Finance.
    """
    print(f"Fetching data for {ticker_symbol}...")
    try:
        ticker = yf.Ticker(ticker_symbol)
        # Get historical market data
        hist = ticker.history(period=period)
        if hist.empty:
            print(f"No data found for {ticker_symbol}")
            return None
        return hist
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def calculate_moving_averages(data, short_window=20, long_window=50):
    """
    Calculates Short (20-day) and Long (50-day) Simple Moving Averages.
    """
    if data is None or len(data) < long_window:
        print("Not enough data to calculate moving averages.")
        return data

    data['SMA_20'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_50'] = data['Close'].rolling(window=long_window).mean()
    return data

def decision_engine(data):
    """
    Determines Buy/Sell/Hold based on SMA crossover strategy.
    Returns BUY only on Golden Cross, SELL only on Death Cross, else HOLD (Trend Continues).
    """
    if data is None or 'SMA_20' not in data.columns or 'SMA_50' not in data.columns:
        return "INSUFFICIENT_DATA"

    # Need at least 2 data points to check for crossover
    if len(data) < 2:
        return "INSUFFICIENT_DATA_FOR_CROSSOVER"

    # Get the last two data points
    today = data.iloc[-1]
    yesterday = data.iloc[-2]
    
    today_short = today['SMA_20']
    today_long = today['SMA_50']
    
    prev_short = yesterday['SMA_20']
    prev_long = yesterday['SMA_50']

    # Check if calculation resulted in NaN
    if pd.isna(today_short) or pd.isna(today_long) or pd.isna(prev_short) or pd.isna(prev_long):
         return "INSUFFICIENT_DATA"

    price = today['Close']
    print(f"Current Price: ${price:.2f}")
    print(f"SMA 20: ${today_short:.2f} (Prev: ${prev_short:.2f})")
    print(f"SMA 50: ${today_long:.2f} (Prev: ${prev_long:.2f})")

    # Check for Golden Cross (Short crosses above Long)
    if prev_short < prev_long and today_short > today_long:
        return "BUY (Golden Cross Signal)"
    
    # Check for Death Cross (Short crosses below Long)
    elif prev_short > prev_long and today_short < today_long:
        return "SELL (Death Cross Signal)"
    
    # No crossover
    else:
        trend = "Uptrend" if today_short > today_long else "Downtrend"
        return f"HOLD (No new crossover, current: {trend})"

def main():
    while True:
        ticker_symbol = input("\nEnter ticker symbol (or 'q' to quit): ").upper()
        if ticker_symbol == 'Q':
            break

        print(f"\n--- Analyzing {ticker_symbol} ---")
        
        # 1. Fetch Data
        stock_data = fetch_data(ticker_symbol)
        
        if stock_data is not None:
            # 2. Calculate Moving Averages
            stock_data = calculate_moving_averages(stock_data)
            
            # 3. Apply Decision Engine
            decision = decision_engine(stock_data)
            
            print(f"Decision for {ticker_symbol}: {decision}")

if __name__ == "__main__":
    main()
