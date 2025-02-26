import time
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, SYMBOL, TIMEFRAME
from data import fetch_data, add_macd
from strategy import macd_strategy
from trading import execute_trade

def run_trading_bot():
    print("Starting MACD Momentum Trading Bot...")
    while True:
        # Fetch and process data
        df = fetch_data(ALPACA_API_KEY, ALPACA_SECRET_KEY, SYMBOL, TIMEFRAME)
        df = add_macd(df)
        
        # Get trading signal
        signal = macd_strategy(df)
        print(f"Signal: {signal}")
        
        # Execute trade
        if signal in ["buy", "sell"]:
            execute_trade(ALPACA_API_KEY, ALPACA_SECRET_KEY, SYMBOL, signal)
        
        # Wait for the next bar (e.g., 1 minute)
        time.sleep(60)

if __name__ == "__main__":
    run_trading_bot()