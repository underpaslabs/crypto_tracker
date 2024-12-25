## Cryptocurrency Price Tracker

A real-time cryptocurrency price tracker with alert functionality built in Python.

### Features
- Real-time price tracking for multiple cryptocurrencies
- Configurable alert thresholds for price changes
- Multiple notification methods (console, file logging)
- Historical data storage in JSON and CSV formats
- Easy-to-configure settings

### Installation

1. **Clone or download the files** into a directory
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Configure the tracker** by editing `config.py`:
   - Add/remove cryptocurrencies from `CRYPTOCURRENCIES` list
   - Adjust `UPDATE_INTERVAL` (in seconds) for how often to check prices
   - Modify `ALERT_THRESHOLDS` for price change percentages
   - Choose notification methods in `NOTIFICATION_METHODS`

2. **Run the tracker**:
   ```bash
   python main.py
   ```

3. **Monitor prices and alerts** in the console
4. **Check log files**:
   - `price_alerts.log` - Contains all triggered alerts
   - `price_history.csv` - Historical price data for analysis
   - `price_data.json` - Raw price data in JSON format

### File Structure
- `config.py` - Configuration settings
- `price_fetcher.py` - API communication for price data
- `alert_manager.py` - Alert detection and notification
- `data_storage.py` - Data persistence and management
- `main.py` - Main application entry point
- `requirements.txt` - Python dependencies

### Customization

**Add new cryptocurrencies**: Edit the `CRYPTOCURRENCIES` list in `config.py` using CoinGecko API IDs.

**Modify alert thresholds**: Change values in `ALERT_THRESHOLDS` dictionary in `config.py`.

**Add email notifications**: Implement the `_email_notification` method in `alert_manager.py` with your email service.

### Dependencies
- `requests` - For HTTP API calls to CoinGecko

The tracker uses the free CoinGecko API which doesn't require an API key for basic price data.