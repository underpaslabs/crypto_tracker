"""
Module for managing price alerts and notifications
"""
import json
import datetime
from config import ALERT_THRESHOLDS, NOTIFICATION_METHODS, LOG_FILE

class AlertManager:
    def __init__(self):
        self.price_history = {}
        self.alert_count = 0
        
    def check_alerts(self, current_prices, previous_prices):
        """Check if any alerts should be triggered based on price changes"""
        alerts = []
        
        for crypto_id, current_data in current_prices.items():
            if crypto_id not in previous_prices:
                continue
                
            prev_data = previous_prices[crypto_id]
            
            # Calculate percentage changes
            current_price = current_data.get('usd', 0)
            previous_price = prev_data.get('usd', 0)
            
            if previous_price > 0:
                price_change_pct = ((current_price - previous_price) / previous_price) * 100
                
                # Check for price increase alert
                if price_change_pct >= ALERT_THRESHOLDS["price_increase"]:
                    alerts.append({
                        'type': 'PRICE_INCREASE',
                        'crypto': crypto_id,
                        'current_price': current_price,
                        'change_pct': price_change_pct,
                        'timestamp': datetime.datetime.now()
                    })
                
                # Check for price decrease alert
                elif price_change_pct <= -ALERT_THRESHOLDS["price_decrease"]:
                    alerts.append({
                        'type': 'PRICE_DECREASE', 
                        'crypto': crypto_id,
                        'current_price': current_price,
                        'change_pct': price_change_pct,
                        'timestamp': datetime.datetime.now()
                    })
        
        return alerts
    
    def send_notification(self, alert):
        """Send notification based on configured methods"""
        message = self._format_alert_message(alert)
        
        for method in NOTIFICATION_METHODS:
            if method == "console":
                self._console_notification(message)
            elif method == "file":
                self._file_notification(message)
            elif method == "email":
                self._email_notification(message)
    
    def _format_alert_message(self, alert):
        """Format alert message for notification"""
        symbol = "🟢" if alert['type'] == 'PRICE_INCREASE' else "🔴"
        direction = "increased" if alert['type'] == 'PRICE_INCREASE' else "decreased"
        
        return (f"{symbol} ALERT: {alert['crypto'].upper()} {direction} by "
                f"{alert['change_pct']:.2f}% to ${alert['current_price']:.2f} "
                f"at {alert['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
    
    def _console_notification(self, message):
        """Send notification to console"""
        print(f"\n{'='*60}")
        print(message)
        print(f"{'='*60}\n")
    
    def _file_notification(self, message):
        """Log notification to file"""
        with open(LOG_FILE, 'a') as f:
            f.write(message + '\n')
    
    def _email_notification(self, message):
        """Send email notification (placeholder)"""
        # This would require email configuration
        print(f"EMAIL NOTIFICATION: {message}")