# Cryptocurrency Price Tracker

A real-time cryptocurrency price tracker with alert functionality built in Python.

## Features

- 📊 Real-time price tracking for multiple cryptocurrencies
- 🔔 Price change alerts with configurable thresholds
- 💾 Historical price data storage
- ⚙️ Easy configuration and customization
- 🎯 Console-based alerts and notifications

## Installation

1. **Clone or download the files** to a directory
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure the tracker** by editing `config.py`:
   - Add/remove cryptocurrencies in `CRYPTOCURRENCIES`
   - Set alert thresholds and update intervals
   - Configure price change percentage for alerts

2. **Run the tracker**:
   ```bash
   python crypto_tracker.py
   ```

3. **The tracker will**:
   - Display current prices every 60 seconds (configurable)
   - Show alerts when prices change significantly
   - Store price history in `price_history.json`

## Configuration Options

- **CRYPTOCURRENCIES**: Dictionary of cryptocurrencies to track
- **UPDATE_INTERVAL**: Seconds between price checks (default: 60)
- **PRICE_CHANGE_THRESHOLD**: Percentage change to trigger alerts (default: 5%)
- **ALERT_ENABLED**: Enable/disable alert system

## Adding New Cryptocurrencies

Edit the `CRYPTOCURRENCIES` dictionary in `config.py`:
```python
CRYPTOCURRENCIES = {
    'bitcoin': {'symbol': 'BTC', 'alert_threshold': 50000},
    'ethereum': {'symbol': 'ETH', 'alert_threshold': 3000},
    # Add new entries using CoinGecko API IDs
    'your-crypto-id': {'symbol': 'SYMBOL', 'alert_threshold': PRICE},
}
```

## Files Structure

- `config.py` - Configuration settings
- `price_fetcher.py` - API communication for price data
- `alert_manager.py` - Alert generation and management
- `data_storage.py` - Historical data storage
- `crypto_tracker.py` - Main application
- `requirements.txt` - Python dependencies

## Stopping the Tracker

Press `Ctrl+C` to gracefully stop the price tracker.

## Notes

- Uses CoinGecko Free API (no API key required)
- Rate limits apply - respect the API terms of service
- Historical data is stored locally in JSON format
- Alerts are shown in console; can be extended for email/desktop notifications