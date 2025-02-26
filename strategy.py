def macd_strategy(df):
    """
    Momentum strategy: Buy when MACD crosses above signal line, sell when it crosses below.
    Returns: "buy", "sell", or "hold"
    """
    if len(df) < 2:
        return "hold"
    
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    
    # Buy signal: MACD crosses above signal
    if (previous["MACD_12_26_9"] < previous["MACDs_12_26_9"]) and \
       (latest["MACD_12_26_9"] > latest["MACDs_12_26_9"]):
        return "buy"
    
    # Sell signal: MACD crosses below signal
    elif (previous["MACD_12_26_9"] > previous["MACDs_12_26_9"]) and \
         (latest["MACD_12_26_9"] < latest["MACDs_12_26_9"]):
        return "sell"
    
    return "hold"