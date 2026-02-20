# Binance Futures Testnet Trading Bot

## Setup

1. Create virtual environment:
   python -m venv venv

2. Activate environment:
   Windows: venv\Scripts\activate
   Mac/Linux: source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create a .env file in root:

   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_secret_key

## Run Examples

Market Order:
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

Logs are stored in:
logs/trading_bot.log
