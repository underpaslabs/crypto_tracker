"""
Module for fetching cryptocurrency prices from CoinGecko API
"""
import requests
import time
from config import COINGECKO_API_URL, CRYPTOCURRENCIES

class PriceFetcher:
    def __init__(self):
        self.base_url = COINGECKO_API_URL
        self.session = requests.Session()
        
    def get_current_prices(self):
        """Fetch current prices for all tracked cryptocurrencies"""
        try:
            # Join cryptocurrency IDs for batch request
            ids = ",".join(CRYPTOCURRENCIES)
            
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': ids,
                'vs_currencies': 'usd',
                'include_24hr_vol': 'true',
                'include_24hr_change': 'true',
                'include_last_updated_at': 'true'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
    
    def get_price_history(self, crypto_id, days=1):
        """Fetch historical price data for a specific cryptocurrency"""
        try:
            url = f"{self.base_url}/coins/{crypto_id}/market_chart"
            params = {
                'vs_currency': 'usd',
                'days': days
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching history for {crypto_id}: {e}")
            return {}