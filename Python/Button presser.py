import time
import pyautogui

def press_key_after_delay(key, delay):
    """
    Presses a specified key after a given delay.

    :param key: The key to press (e.g., 'a', 'enter', 'space').
    :param delay: The delay in seconds before pressing the key.
    """
    print(f"Waiting for {delay} seconds before pressing '{key}'...")
    time.sleep(delay)
    pyautogui.press(key)
    print(f"'{key}' key pressed.")

# Example usage
press_key_after_delay('v', 5)  # Presses the 'a' key after 5 seconds
