# Cryptocurrency Price Tracker

A real-time cryptocurrency price tracker with alert functionality.

## Features

- 📊 Real-time price tracking for major cryptocurrencies
- 🔔 Custom price alerts with visual and audio notifications
- 📈 24-hour price change indicators
- ⚙️ Configurable settings and thresholds
- 🎯 Easy-to-use terminal interface

## Installation

1. **Clone or download the script files** to a directory

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure your settings** in `config.py`:
   - Modify `CRYPTOCURRENCIES` to track different coins
   - Adjust `ALERT_THRESHOLDS` for your price targets
   - Change `UPDATE_INTERVAL` for update frequency

2. **Run the tracker**:
   ```bash
   python price_tracker.py
   ```

## Configuration Options

### Tracked Cryptocurrencies
Edit the `CRYPTOCURRENCIES` dictionary in `config.py`:
```python
CRYPTOCURRENCIES = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    # Add more: "coin-id": "SYMBOL"
}
```

### Price Alerts
Set high/low thresholds in `ALERT_THRESHOLDS`:
```python
ALERT_THRESHOLDS = {
    "BTC": {"high": 50000, "low": 40000},
    # Add thresholds for other coins
}
```

### Update Frequency
Change `UPDATE_INTERVAL` in seconds (default: 60 seconds)

## Files Overview

- `config.py` - Configuration settings
- `price_fetcher.py` - API data fetching
- `alert_manager.py` - Alert handling and notifications
- `price_tracker.py` - Main application
- `requirements.txt` - Python dependencies

## Supported Cryptocurrencies

The script uses CoinGecko API, which supports thousands of cryptocurrencies. Use the CoinGecko ID for any cryptocurrency you want to track.

## Troubleshooting

- **No data displayed**: Check internet connection and API availability
- **Alerts not working**: Verify alert thresholds in config.py
- **Import errors**: Ensure all files are in the same directory

## License

Free for personal and educational use.

---

**Note**: This script uses the free CoinGecko API which has rate limits. For heavy usage, consider getting an API key.