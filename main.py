"""
Main script for cryptocurrency price tracker
"""
import time
import sys
from datetime import datetime
from price_fetcher import PriceFetcher
from alert_manager import AlertManager
from data_storage import DataStorage
from config import UPDATE_INTERVAL, CRYPTOCURRENCIES

class CryptoTracker:
    def __init__(self):
        self.price_fetcher = PriceFetcher()
        self.alert_manager = AlertManager()
        self.data_storage = DataStorage()
        self.running = False
        
    def display_prices(self, prices):
        """Display current prices in a formatted way"""
        print(f"\n{'='*80}")
        print(f"CRYPTOCURRENCY PRICES - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*80}")
        print(f"{'CRYPTOCURRENCY':<15} {'PRICE (USD)':<15} {'24H CHANGE':<12} {'24H VOLUME':<15}")
        print(f"{'-'*80}")
        
        for crypto in CRYPTOCURRENCIES:
            if crypto in prices:
                data = prices[crypto]
                price = data.get('usd', 0)
                change = data.get('usd_24h_change', 0)
                volume = data.get('usd_24h_vol', 0)
                
                change_str = f"{change:+.2f}%"
                change_color = "\033[92m" if change >= 0 else "\033[91m"  # Green for positive, red for negative
                reset_color = "\033[0m"
                
                print(f"{crypto.upper():<15} ${price:<14.2f} {change_color}{change_str:<12}{reset_color} ${volume:,.0f}")
        
        print(f"{'='*80}")
    
    def run(self):
        """Main tracking loop"""
        self.running = True
        print("🚀 Cryptocurrency Price Tracker Started!")
        print("Press Ctrl+C to stop...")
        
        previous_prices = self.data_storage.load_previous_prices()
        
        try:
            while self.running:
                # Fetch current prices
                current_prices = self.price_fetcher.get_current_prices()
                
                if current_prices:
                    # Display prices
                    self.display_prices(current_prices)
                    
                    # Save data
                    self.data_storage.save_prices(current_prices)
                    self.data_storage.save_to_csv(current_prices)
                    
                    # Check for alerts if we have previous data
                    if previous_prices:
                        alerts = self.alert_manager.check_alerts(current_prices, previous_prices)
                        for alert in alerts:
                            self.alert_manager.send_notification(alert)
                    
                    # Update previous prices for next iteration
                    previous_prices = current_prices.copy()
                
                # Wait for next update
                time.sleep(UPDATE_INTERVAL)
                
        except KeyboardInterrupt:
            print("\n\n🛑 Price tracker stopped by user")
            self.running = False
        except Exception as e:
            print(f"\n❌ Error in main loop: {e}")
            self.running = False

def main():
    tracker = CryptoTracker()
    tracker.run()

if __name__ == "__main__":
    main()