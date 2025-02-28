from data import fetch_data, add_macd
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, SYMBOL, TIMEFRAME
from strategy import macd_strategy
import pandas as pd

def backtest(api_key, secret_key, symbol, timeframe, limit=1000):
    # Fetch historical data
    df = fetch_data(api_key, secret_key, symbol, timeframe, limit)
    if df is None or df.empty:
        print("Error: No data received")
        return
        
    df = add_macd(df)
    
    # Initialize tracking variables
    initial_cash = 10000
    cash = initial_cash
    position = 0
    trades = []

    # Iterate through the dataframe to generate signals and execute trades
    for i in range(1, len(df)):
        signal = macd_strategy(df.iloc[:i+1])
        price = df.iloc[i]["close"]
        timestamp = df.index[i]
        
        if signal == "buy" and cash >= price:
            shares_to_buy = int(cash // price)
            if shares_to_buy > 0:
                position += shares_to_buy
                cash -= shares_to_buy * price
                trades.append({
                    "type": "BUY",
                    "price": price,
                    "shares": shares_to_buy,
                    "timestamp": timestamp,
                    "macd": df.iloc[i]["MACD_12_26_9"],
                    "signal": df.iloc[i]["MACDs_12_26_9"]
                })
                print(f"BUY: {shares_to_buy} shares @ ${price:.2f} on {timestamp}")
                print(f"MACD: {df.iloc[i]['MACD_12_26_9']:.6f}, Signal: {df.iloc[i]['MACDs_12_26_9']:.6f}")
                print(f"Previous MACD: {df.iloc[i-1]['MACD_12_26_9']:.6f}, Previous Signal: {df.iloc[i-1]['MACDs_12_26_9']:.6f}\n")
        
        elif signal == "sell" and position > 0:
            cash += position * price
            trades.append({
                "type": "SELL",
                "price": price,
                "shares": position,
                "timestamp": timestamp,
                "macd": df.iloc[i]["MACD_12_26_9"],
                "signal": df.iloc[i]["MACDs_12_26_9"]
            })
            print(f"SELL: {position} shares @ ${price:.2f} on {timestamp}")
            print(f"MACD: {df.iloc[i]['MACD_12_26_9']:.6f}, Signal: {df.iloc[i]['MACDs_12_26_9']:.6f}")
            print(f"Previous MACD: {df.iloc[i-1]['MACD_12_26_9']:.6f}, Previous Signal: {df.iloc[i-1]['MACDs_12_26_9']:.6f}\n")
            position = 0
    
    # Calculate performance metrics
    final_value = cash + position * df.iloc[-1]["close"]
    returns = ((final_value - initial_cash) / initial_cash) * 100
    
    print(f"\nSummary:")
    print(f"Initial Portfolio Value: ${initial_cash:.2f}")
    print(f"Final Portfolio Value: ${final_value:.2f}")
    print(f"Return: {returns:.2f}%")
    print(f"Number of trades: {len(trades)}")
    
    return trades, final_value, returns

# Run backtest
backtest(ALPACA_API_KEY, ALPACA_SECRET_KEY, SYMBOL, "1Min", 80)