import pyautogui
import time

try:
    print("Mouse wiggler started. Press Ctrl+C to stop.")
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()

        # Move the mouse slightly (e.g., by 1 pixel and back)
        pyautogui.moveTo(x + 1, y + 1)
        time.sleep(0.1)
        pyautogui.moveTo(x, y)

        # Wait for 10 seconds before wiggling again
        time.sleep(5)

except KeyboardInterrupt:
    print("Mouse wiggler stopped.")
