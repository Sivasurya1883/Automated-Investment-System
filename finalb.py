import subprocess

import pyautogui
import time
time.sleep(5)
click_x = 247
click_y = 120
time.sleep(3)
pyautogui.click(click_x, click_y)
time.sleep(10)
click_x=678
click_y=517

pyautogui.click(click_x, click_y)
time.sleep(10)
#clicks portfolio
click_x=688
click_y=738

pyautogui.click(click_x, click_y)
def take_screenshot():
        time.sleep(5)
        screenshot = pyautogui.screenshot()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"C:/Users/Blaze/Desktop/sample/images1/{timestamp}.png"
        screenshot.save(screenshot_path)
        return screenshot_path

screenshot_path = take_screenshot()
pyautogui.press('f11')

time.sleep(10)
click_x = 858
click_y = 120
time.sleep(3)
pyautogui.click(click_x, click_y)
time.sleep(5)
click_x=678
click_y=517

pyautogui.click(click_x, click_y)
time.sleep(10)
#clicks portfolio
click_x=688
click_y=738

pyautogui.click(click_x, click_y)
def take_screenshot():
        time.sleep(5)
        screenshot = pyautogui.screenshot()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"C:/Users/Blaze/Desktop/sample/images1/{timestamp}.png"
        screenshot.save(screenshot_path)
        return screenshot_path
