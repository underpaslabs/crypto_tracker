"""
Configuration file for cryptocurrency price tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
UPDATE_INTERVAL = 60  # seconds

# Cryptocurrencies to track (symbol: name)
CRYPTOCURRENCIES = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "cardano": "ADA",
    "solana": "SOL",
    "ripple": "XRP"
}

# Alert Configuration
ALERT_THRESHOLDS = {
    "BTC": {"high": 50000, "low": 40000},
    "ETH": {"high": 3000, "low": 2000},
    "ADA": {"high": 1.5, "low": 0.8},
    "SOL": {"high": 200, "low": 100},
    "XRP": {"high": 1.0, "low": 0.5}
}

# Notification Settings
ENABLE_ALERTS = True
ALERT_SOUND = True