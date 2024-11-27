"""
Main cryptocurrency price tracker application
"""
import time
import sys
from datetime import datetime
from price_fetcher import PriceFetcher
from alert_manager import AlertManager
from data_storage import DataStorage
from config import CRYPTOCURRENCIES, UPDATE_INTERVAL, CURRENCY

class CryptoTracker:
    def __init__(self):
        self.price_fetcher = PriceFetcher()
        self.alert_manager = AlertManager()
        self.data_storage = DataStorage()
        self.running = False
        
    def display_prices(self, crypto_data):
        """Display current prices in a formatted way"""
        print(f"\n{'='*60}")
        print(f"🔄 CRYPTO PRICE TRACKER - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")
        
        for crypto_id, config in CRYPTOCURRENCIES.items():
            if crypto_id in crypto_data:
                data = crypto_data[crypto_id]
                price = data.get('usd', 'N/A')
                change_24h = data.get('usd_24h_change', 0)
                
                if price != 'N/A':
                    change_symbol = "📈" if change_24h > 0 else "📉" if change_24h < 0 else "➡️"
                    print(f"{config['symbol']}: ${price:,.2f} {change_symbol} {change_24h:+.2f}%")
                else:
                    print(f"{config['symbol']}: Data unavailable")
        
        print(f"{'='*60}")
    
    def run(self):
        """Main tracking loop"""
        self.running = True
        print("🚀 Starting Cryptocurrency Price Tracker...")
        print("Press Ctrl+C to stop\n")
        
        try:
            while self.running:
                # Fetch current prices
                crypto_data = self.price_fetcher.get_prices()
                
                if crypto_data:
                    # Get previous prices for comparison
                    previous_prices = self.data_storage.get_previous_prices()
                    
                    # Display current prices
                    self.display_prices(crypto_data)
                    
                    # Check and display alerts
                    alerts = self.alert_manager.check_price_alerts(crypto_data, previous_prices)
                    self.alert_manager.send_console_alert(alerts)
                    
                    # Save data to history
                    self.data_storage.save_price_data(crypto_data)
                
                # Wait for next update
                time.sleep(UPDATE_INTERVAL)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Price tracker stopped by user")
            self.stop()
        except Exception as e:
            print(f"\n❌ Error in main loop: {e}")
            self.stop()
    
    def stop(self):
        """Stop the tracker"""
        self.running = False

def main():
    tracker = CryptoTracker()
    tracker.run()

if __name__ == "__main__":
    main()