# Script that takes screenshots via a hotkey (Alt + some key)
# Usage: python screenshot.py [hotkey] [save_path]

import pyautogui
import keyboard
import datetime
import sys
import os

hotkey = "alt+" + sys.argv[1] if len(sys.argv) > 1 else "alt+x"


def takeScreenshot():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    save_path = f"D:\\User\\Pictures\\{current_time}.png"

    if len(sys.argv) > 2:
        if os.path.exists(sys.argv[2]):
            save_path = f"{sys.argv[2]}\\{current_time}.png"
        else:
            print("Path invalid.")
            quit()

    pyautogui.screenshot(save_path)


keyboard.add_hotkey(hotkey, takeScreenshot)

try:
    keyboard.wait()
except KeyboardInterrupt:
    quit()
