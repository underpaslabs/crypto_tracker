"""
Configuration file for cryptocurrency price tracker
"""

# API Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
UPDATE_INTERVAL = 60  # seconds

# Cryptocurrencies to track
CRYPTOCURRENCIES = [
    "bitcoin",
    "ethereum", 
    "cardano",
    "solana",
    "dogecoin"
]

# Alert thresholds (percentage change)
ALERT_THRESHOLDS = {
    "price_increase": 5.0,   # Alert if price increases by 5%
    "price_decrease": 5.0,   # Alert if price decreases by 5%
    "volume_spike": 50.0     # Alert if volume increases by 50%
}

# Notification settings
NOTIFICATION_METHODS = ["console", "file"]  # Options: "console", "file", "email"
LOG_FILE = "price_alerts.log"