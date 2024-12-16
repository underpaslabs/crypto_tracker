"""
Module for storing and managing price data
"""
import json
import csv
import os
from datetime import datetime

class DataStorage:
    def __init__(self, storage_file="price_data.json"):
        self.storage_file = storage_file
        self.csv_file = "price_history.csv"
        self._initialize_storage()
    
    def _initialize_storage(self):
        """Initialize storage files if they don't exist"""
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({}, f)
        
        # Initialize CSV with headers if it doesn't exist
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'cryptocurrency', 'price_usd', 'volume_24h', 'change_24h'])
    
    def save_prices(self, prices):
        """Save current prices to JSON storage"""
        try:
            timestamp = datetime.now().isoformat()
            data = {
                'timestamp': timestamp,
                'prices': prices
            }
            
            with open(self.storage_file, 'r+') as f:
                existing_data = json.load(f)
                existing_data[timestamp] = prices
                f.seek(0)
                json.dump(existing_data, f, indent=2)
                
        except Exception as e:
            print(f"Error saving prices: {e}")
    
    def save_to_csv(self, prices):
        """Append prices to CSV file for historical analysis"""
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            with open(self.csv_file, 'a', newline='') as f:
                writer = csv.writer(f)
                
                for crypto_id, data in prices.items():
                    writer.writerow([
                        timestamp,
                        crypto_id,
                        data.get('usd', 0),
                        data.get('usd_24h_vol', 0),
                        data.get('usd_24h_change', 0)
                    ])
                    
        except Exception as e:
            print(f"Error saving to CSV: {e}")
    
    def load_previous_prices(self):
        """Load the most recent previous prices for comparison"""
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
            
            if not data:
                return {}
            
            # Get the most recent entry
            latest_timestamp = sorted(data.keys())[-1]
            return data[latest_timestamp]
            
        except Exception as e:
            print(f"Error loading previous prices: {e}")
            return {}