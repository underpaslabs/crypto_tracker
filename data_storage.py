"""
Module for storing and managing price history
"""
import json
import os
from datetime import datetime

class DataStorage:
    def __init__(self, history_file='price_history.json'):
        self.history_file = history_file
        self.price_history = self.load_history()
        
    def load_history(self):
        """Load price history from file"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, Exception):
                return {}
        return {}
    
    def save_price_data(self, crypto_data):
        """Save current prices to history"""
        timestamp = datetime.now().isoformat()
        
        for crypto_id, data in crypto_data.items():
            if crypto_id not in self.price_history:
                self.price_history[crypto_id] = []
            
            price_entry = {
                'timestamp': timestamp,
                'price': data.get('usd'),
                'change_24h': data.get('usd_24h_change', 0)
            }
            
            self.price_history[crypto_id].append(price_entry)
            
            # Keep only last 1000 entries per cryptocurrency
            if len(self.price_history[crypto_id]) > 1000:
                self.price_history[crypto_id] = self.price_history[crypto_id][-1000:]
        
        self._save_to_file()
    
    def _save_to_file(self):
        """Save history to JSON file"""
        try:
            with open(self.history_file, 'w') as f:
                json.dump(self.price_history, f, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def get_previous_prices(self):
        """Get the most recent previous prices for each cryptocurrency"""
        previous_prices = {}
        for crypto_id, history in self.price_history.items():
            if history:
                previous_prices[crypto_id] = history[-1]['price']
        return previous_prices