from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

def execute_trade(api_key, secret_key, symbol, action, qty=1):
    trading_client = TradingClient(api_key, secret_key, paper=True)
    
    if action == "buy":
        order = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.BUY,
            time_in_force=TimeInForce.GTC
        )
        trading_client.submit_order(order)
        print(f"Placed BUY order for {qty} shares of {symbol}")
    
    elif action == "sell":
        order = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC
        )
        trading_client.submit_order(order)
        print(f"Placed SELL order for {qty} shares of {symbol}")