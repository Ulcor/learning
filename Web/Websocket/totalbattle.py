import json
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# Start Chrome with DevTools access
options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)

# Go to the game page
driver.get('https://totalbattle.com/en/')

# Add your session cookie
driver.add_cookie({
    'name': 'special_iprops32',
    'value': 'your_token_here',  # <-- put your real token here
    'domain': 'totalbattle.com',
    'path': '/',
})
driver.refresh()

# Enable network monitoring
driver.execute_cdp_cmd('Network.enable', {})
driver.execute_cdp_cmd('Network.setCacheDisabled', {'cacheDisabled': True})

# Subscribe to WebSocket frames
driver.execute_cdp_cmd('Network.enable', {})
print("[+] Listening for WebSocket frames...")

# Storage for WebSocket frames
websocket_messages = []

# Poll WebSocket frames
try:
    while True:
        logs = driver.get_log('performance')
        for entry in logs:
            message = json.loads(entry['message'])['message']
            if message['method'] == 'Network.webSocketFrameReceived':
                payload_data = message['params']['response']['payloadData']

                # You can print raw payload
                print(f"[WebSocket Frame] {payload_data}")

                # Try to parse as JSON
                try:
                    event = json.loads(payload_data)
                    print(f"✅ Parsed Event: {event}")
                    websocket_messages.append(event)
                except Exception as e:
                    print(f"❌ Cannot parse frame: {e}")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("[*] Stopping WebSocket listener.")
    driver.quit()
