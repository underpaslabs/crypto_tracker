"""
Module for fetching cryptocurrency prices from CoinGecko API
"""
import requests
import time
from config import COINGECKO_API_URL, CRYPTOCURRENCIES, CURRENCY

class PriceFetcher:
    def __init__(self):
        self.session = requests.Session()
        
    def get_prices(self):
        """Fetch current prices for all tracked cryptocurrencies"""
        try:
            crypto_ids = ','.join(CRYPTOCURRENCIES.keys())
            params = {
                'ids': crypto_ids,
                'vs_currencies': CURRENCY,
                'include_24hr_change': 'true'
            }
            
            response = self.session.get(COINGECKO_API_URL, params=params, timeout=10)
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {}