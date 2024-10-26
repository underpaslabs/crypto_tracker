"""
Module to fetch cryptocurrency prices from CoinGecko API
"""
import requests
import time
from config import COINGECKO_API_URL, CRYPTOCURRENCIES

class PriceFetcher:
    def __init__(self):
        self.base_url = COINGECKO_API_URL
    
    def get_prices(self):
        """
        Fetch current prices for all tracked cryptocurrencies
        Returns dict with symbol: price
        """
        try:
            # Get cryptocurrency IDs for the API
            crypto_ids = list(CRYPTOCURRENCIES.keys())
            ids_param = ",".join(crypto_ids)
            
            # Make API request
            url = f"{self.base_url}/simple/price"
            params = {
                'ids': ids_param,
                'vs_currencies': 'usd',
                'include_24hr_change': 'true'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Process and return prices
            prices = {}
            for crypto_id, crypto_data in data.items():
                symbol = CRYPTOCURRENCIES[crypto_id]
                prices[symbol] = {
                    'price': crypto_data['usd'],
                    'change_24h': crypto_data.get('usd_24h_change', 0),
                    'timestamp': time.time()
                }
            
            return prices
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {}

if __name__ == "__main__":
    fetcher = PriceFetcher()
    prices = fetcher.get_prices()
    print("Sample price data:", prices)