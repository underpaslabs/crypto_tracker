"""
Module to manage price alerts and notifications
"""
import os
import time
from config import ALERT_THRESHOLDS, ENABLE_ALERTS, ALERT_SOUND

class AlertManager:
    def __init__(self):
        self.triggered_alerts = set()
    
    def check_alerts(self, symbol, price):
        """
        Check if price triggers any alerts
        Returns list of alert messages
        """
        if not ENABLE_ALERTS or symbol not in ALERT_THRESHOLDS:
            return []
        
        alerts = []
        thresholds = ALERT_THRESHOLDS[symbol]
        alert_key = f"{symbol}_{price}"
        
        # Check high threshold
        if price >= thresholds["high"] and f"{symbol}_high" not in self.triggered_alerts:
            alert_msg = f"🚨 ALERT: {symbol} reached ${price:,.2f} (above ${thresholds['high']:,.2f})"
            alerts.append(alert_msg)
            self.triggered_alerts.add(f"{symbol}_high")
        
        # Check low threshold
        elif price <= thresholds["low"] and f"{symbol}_low" not in self.triggered_alerts:
            alert_msg = f"🚨 ALERT: {symbol} dropped to ${price:,.2f} (below ${thresholds['low']:,.2f})"
            alerts.append(alert_msg)
            self.triggered_alerts.add(f"{symbol}_low")
        
        # Reset alerts if price returns to normal range
        elif thresholds["low"] < price < thresholds["high"]:
            self.triggered_alerts.discard(f"{symbol}_high")
            self.triggered_alerts.discard(f"{symbol}_low")
        
        return alerts
    
    def notify(self, message):
        """
        Display notification and play sound if enabled
        """
        print(f"\n{'='*60}")
        print(message)
        print(f"{'='*60}\n")
        
        if ALERT_SOUND:
            # Play system alert sound
            try:
                # For Windows
                if os.name == 'nt':
                    import winsound
                    winsound.MessageBeep()
                # For macOS/Linux
                else:
                    print('\a')  # Terminal bell
            except:
                pass  # Silently fail if sound not available

if __name__ == "__main__":
    manager = AlertManager()
    # Test alerts
    test_alerts = manager.check_alerts("BTC", 51000)
    for alert in test_alerts:
        manager.notify(alert)