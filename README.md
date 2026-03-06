# 🚀 Simple Python CLI Trading Bot

A modular Python-based Command Line Interface (CLI) bot for placing orders on the **Binance Futures Testnet (USDT-M)**. Designed for reliability, security, and clean code architecture.

## 🛠️ Features
- **Modular Architecture**: Separate logic for API connection, validation, and order execution.
- **Validation**: Strict input checking for symbols, sides (BUY/SELL), and order types to prevent unnecessary API errors.
- **Logging**: Comprehensive audit trail stored in `logs/bot.log` including request payloads and exchange responses.
- **Security**: Environment variable support via `.env` to ensure API secrets are never hardcoded.



---

## 🚀 Setup

### 1. Clone & Install
```bash
git clone [https://github.com/Pradesha3112/trading_bot.git](https://github.com/Pradesha3112/trading_bot.git)
cd trading_bot
pip install -r requirements.txt
```
2. Configure Environment
Create a .env file in the root directory (this file is ignored by Git for security):

Plaintext
```bash
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

Usage Examples
The bot is controlled via cli.py. Use the following commands to test the logic:

MARKET Order
```Bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```
LIMIT Order
```Bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 75000
```

🏗️ Project Architecture
The application is organized into specific modules for maintainability:

cli.py: Entry point handling user arguments and terminal output.

bot/validators.py: Ensures inputs are sanitized and valid before processing.

bot/client.py: Manages the secure authenticated connection to Binance Testnet.

bot/orders.py: Core execution engine for order placement.

bot/logging_config.py: Configures the automated logging system.
