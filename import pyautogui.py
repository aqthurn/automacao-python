import pyautogui
import time



# Press "Alt+Tab" to switch windows
pyautogui.hotkey("alt", "tab")
time.sleep(3)

# Repeat the click at position (1306, 442) five times
repeats = 4
for _ in range(repeats):
    pyautogui.click(x=1306, y=442)
    time.sleep(1)  # Delay of 1 second between each click

# Click 10,000 times at position (100, 100) with a 0.5-second delay
roblox = 10000
for _ in range(roblox):
    pyautogui.click(x=100, y=100)
    time.sleep(0.01)

time.sleep(0.5)
