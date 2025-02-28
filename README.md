<header>

<!--
  <<< Author notes: Course header >>>
  Include a 1280×640 image, course title in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Add your open source license, GitHub uses MIT license.
-->

# Folio-AI
Python License Status

A Python-based trading bot that implements momentum trading strategies using technical indicators like MACD, RSI, and Bollinger Bands. The bot integrates with Alpaca’s Paper Trading API for testing and can be deployed with the Live Trading API. Built with scalability and continuous improvement in mind, it leverages pandas-ta for technical analysis and includes backtesting capabilities.

</header>

## Features
- Momentum Trading: Uses the MACD indicator to generate buy/sell signals based on momentum crossovers.
- Modular Design: Easily extendable to include additional indicators (e.g., RSI, Bollinger Bands) and strategies.
- Alpaca Integration: Supports both paper and live trading via Alpaca’s API.
- Backtesting: Evaluate strategies using historical data.
- Real-Time Execution: Runs continuously with configurable timeframes (e.g., 1-minute bars).
- Create an Alpaca Paper Trading Account
- Input the generated key and secret into the configure.py script 
- Run the main.py script

## Project Structure? 
```
Folio-AI/
├── config.py         # API keys and constants
├── data.py           # Fetch and process market data
├── strategy.py       # Define trading strategies (MACD, RSI, etc.)
├── trading.py        # Execute trades via Alpaca API
├── backtest.py       # Backtesting logic
├── main.py           # Main execution script
├── README.md         # Project documentation
└── requirements.txt  # Dependencies
```

## Prerequisites
- Python 3.8+
- Alpaca Markets account (sign up at alpaca.markets)
- API Key ID and Secret Key (paper trading initially)

## Installation
### 1. Clone the Repository:
  ``` bash
  git clone https://github.com/yourusername/momentum_trading_ai.git
  cd momentum_trading_ai
  ```
### 2. Install Dependencies:
  ``` bash
  pip install -r requirements.txt
  ```
### 3. Configure API Keys:
Open config.py and add your Alpaca API credentials:
``` python
ALPACA_API_KEY = "your_paper_api_key"
ALPACA_SECRET_KEY = "your_paper_secret_key"
ALPACA_BASE_URL = "https://paper-api.alpaca.markets"  # For paper trading
SYMBOL = "AAPL"  # Stock to trade
TIMEFRAME = "1Min"  # Data timeframe
```

## Usage
### 1. Run Paper Trading
  Start the bot in paper trading mode to test the MACD strategy:
  ``` bash 
  python main.py
  ```
  - The bot fetches 1-minute bars, calculates MACD, and places buy/sell orders based on crossovers.
  - Monitor the console for signals and trade confirmations.
### 2. Backtest the Strategy
  Evaluate performance using historical data:
  ``` bash
  python backtest.py
  ```
  - Adjust limit in backtest.py to fetch more historical bars (default: 1000).
### 3. Extend Strategies
  - Add new indicators (e.g., RSI) in data.py and strategy.py.
  - Update main.py to use the new strategy.
### 4. Deploy to Live Trading
#### 1. Update config.py with live API keys and URL:
  ``` python
  ALPACA_API_KEY = "your_live_api_key"
  ALPACA_SECRET_KEY = "your_live_secret_key"
  ALPACA_BASE_URL = "https://api.alpaca.markets"
  ```
#### 2. Set paper=False in trading.py:
  ``` python
  trading_client = TradingClient(api_key, secret_key, paper=False)
  ```
#### 3. Run main.py on a cloud server for continuous execution.

## Requirements
### See requirements.txt:
  ```
  alpaca-py>=0.7.0
  pandas>=1.5.0
  pandas-ta>=0.3.14
  numpy>=1.23.0
  requests>=2.28.0
  ```
## Future Improvements
- Parameter Optimization: Use grid search to tune MACD/RSI parameters.
- Machine Learning: Integrate predictive models for enhanced signals.
- Multi-Asset Support: Trade multiple stocks simultaneously.
- WebSocket Data: Replace polling with real-time streaming.
- Risk Management: Add advanced stop-loss and position sizing.
- Sentiment Analysis: Incorporate market sentiment from external sources (e.g., X posts).

## Contributing
1. Fork the repository.
2. Create a feature branch (git checkout -b feature/new-strategy).
3. Commit changes (git commit -m "Add RSI strategy").
4. Push to the branch (git push origin feature/new-strategy).
5. Open a pull request.

## License
This project is licensed under the MIT License - see LICENSE for details.

## Disclaimer
This bot is for educational purposes only. Trading involves risk, and past performance does not guarantee future results. Test thoroughly in paper trading before using real capital.














