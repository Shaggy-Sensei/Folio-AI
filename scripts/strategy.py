def macd_strategy(df):
    """
    Momentum strategy: Buy when MACD crosses the signal line from below, sell when it crosses the 
    signal line from above.
    Returns: "buy", "sell", or "hold"
    """
    if len(df) < 2:
        return "hold"
    
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    
    previous_signal = previous["MACDs_12_26_9"]
    latest_signal = latest["MACDs_12_26_9"]
    previous_macd = previous["MACD_12_26_9"]
    latest_macd = latest["MACD_12_26_9"]
    
    # Buy signal: MACD crosses above signal
    if (previous_macd < previous_signal) and \
       (latest_macd > latest_signal):
        return "buy"
    
    # Sell signal: MACD crosses below signal
    elif (previous_macd > previous_signal) and \
         (latest_macd < latest_signal):
        return "sell"
    
    return "hold"