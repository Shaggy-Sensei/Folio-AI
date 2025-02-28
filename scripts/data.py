from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
import pandas as pd

def fetch_data(api_key, secret_key, symbol, timeframe, limit=100):
    client = StockHistoricalDataClient(api_key, secret_key)
    request_params = StockBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=TimeFrame.Minute if timeframe == "1Min" else TimeFrame.Day,
        limit=limit
    )
    bars = client.get_stock_bars(request_params).df
    bars = bars.reset_index(level=0, drop=True)  # Remove symbol index
    return bars[["close", "open", "high", "low", "volume"]]

def add_macd(df):
    import pandas_ta as ta
    df.ta.macd(close="close", fast=12, slow=26, signal=9, append=True)
    return df