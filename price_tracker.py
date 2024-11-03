"""
Main cryptocurrency price tracker with real-time updates
"""
import time
import os
from datetime import datetime
from price_fetcher import PriceFetcher
from alert_manager import AlertManager
from config import UPDATE_INTERVAL, CRYPTOCURRENCIES

class CryptoTracker:
    def __init__(self):
        self.price_fetcher = PriceFetcher()
        self.alert_manager = AlertManager()
        self.previous_prices = {}
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_prices(self, prices):
        """Display formatted price information"""
        self.clear_screen()
        print("🪙 CRYPTOCURRENCY PRICE TRACKER")
        print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 80)
        print(f"{'SYMBOL':<8} {'PRICE (USD)':<15} {'24H CHANGE':<12} {'STATUS':<10}")
        print("-" * 80)
        
        for symbol, data in prices.items():
            price = data['price']
            change = data['change_24h']
            
            # Determine trend indicator
            if change > 0:
                trend = "📈"
                change_str = f"+{change:.2f}%"
            elif change < 0:
                trend = "📉"
                change_str = f"{change:.2f}%"
            else:
                trend = "➡️"
                change_str = "0.00%"
            
            # Check if price changed significantly
            status = ""
            if symbol in self.previous_prices:
                prev_price = self.previous_prices[symbol]
                if price > prev_price:
                    status = "🔼"
                elif price < prev_price:
                    status = "🔽"
            
            print(f"{symbol:<8} ${price:>10,.2f} {change_str:>12} {trend:>3} {status:>3}")
        
        print("-" * 80)
        print("Press Ctrl+C to stop tracking")
    
    def run(self):
        """Main tracking loop"""
        print("Starting Cryptocurrency Price Tracker...")
        print("Tracking:", ", ".join(CRYPTOCURRENCIES.values()))
        
        try:
            while True:
                # Fetch current prices
                prices = self.price_fetcher.get_prices()
                
                if prices:
                    # Display prices
                    self.display_prices(prices)
                    
                    # Check for alerts
                    for symbol, data in prices.items():
                        alerts = self.alert_manager.check_alerts(symbol, data['price'])
                        for alert in alerts:
                            self.alert_manager.notify(alert)
                    
                    # Update previous prices
                    self.previous_prices = {symbol: data['price'] for symbol, data in prices.items()}
                else:
                    print("Failed to fetch prices. Retrying...")
                
                # Wait for next update
                time.sleep(UPDATE_INTERVAL)
                
        except KeyboardInterrupt:
            print("\n\n👋 Stopping price tracker. Goodbye!")
        except Exception as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    tracker = CryptoTracker()
    tracker.run()