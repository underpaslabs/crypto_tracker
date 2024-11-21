"""
Module for managing price alerts and notifications
"""
import smtplib
from email.mime.text import MimeText
from config import ALERT_ENABLED, PRICE_CHANGE_THRESHOLD

class AlertManager:
    def __init__(self):
        self.sent_alerts = set()
        
    def check_price_alerts(self, crypto_data, previous_prices):
        """Check if price changes trigger any alerts"""
        alerts = []
        
        for crypto_id, data in crypto_data.items():
            current_price = data.get('usd')
            price_change = data.get('usd_24h_change', 0)
            
            # Check percentage change alert
            if abs(price_change) >= PRICE_CHANGE_THRESHOLD:
                alert_msg = f"🚨 {crypto_id.upper()} changed {price_change:.2f}% in 24h - Current: ${current_price:,.2f}"
                alerts.append(alert_msg)
            
            # Check threshold alert (if previous price exists)
            if crypto_id in previous_prices:
                prev_price = previous_prices[crypto_id]
                if prev_price and current_price:
                    change_pct = ((current_price - prev_price) / prev_price) * 100
                    if abs(change_pct) >= PRICE_CHANGE_THRESHOLD:
                        alert_key = f"{crypto_id}_{change_pct:.1f}"
                        if alert_key not in self.sent_alerts:
                            alert_msg = f"📈 {crypto_id.upper()} changed {change_pct:.2f}% - ${prev_price:,.2f} → ${current_price:,.2f}"
                            alerts.append(alert_msg)
                            self.sent_alerts.add(alert_key)
        
        return alerts
    
    def send_console_alert(self, alerts):
        """Display alerts in console"""
        if alerts and ALERT_ENABLED:
            print("\n" + "="*50)
            print("📢 PRICE ALERTS:")
            for alert in alerts:
                print(f"• {alert}")
            print("="*50 + "\n")