"""
Configuration file for the cryptocurrency price tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
UPDATE_INTERVAL = 60  # seconds between price checks

# Cryptocurrencies to track
CRYPTOCURRENCIES = {
    'bitcoin': {'symbol': 'BTC', 'alert_threshold': 50000},
    'ethereum': {'symbol': 'ETH', 'alert_threshold': 3000},
    'cardano': {'symbol': 'ADA', 'alert_threshold': 1.5},
    'solana': {'symbol': 'SOL', 'alert_threshold': 150},
}

# Alert Configuration
ALERT_ENABLED = True
PRICE_CHANGE_THRESHOLD = 5.0  # percentage change to trigger alert

# Display Configuration
CURRENCY = 'usd'