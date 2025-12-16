from fetch_stock import fetch_data, calculate_moving_averages, decision_engine

def main():
    symbol = "AAPL"
    
    # 1. Fetch Data
    # Note: fetch_data as implemented returns a DataFrame or None
    data = fetch_data(symbol)
    
    if data is not None:
        # 2. Calculate Moving Averages
        # The original script does this sequentially
        data_with_ma = calculate_moving_averages(data)
        
        # 3. Analyze
        decision = decision_engine(data_with_ma)
        
        print(f"Recommendation for {symbol}: {decision}")

if __name__ == "__main__":
    main()
