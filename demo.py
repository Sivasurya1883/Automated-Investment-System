import pyautogui
import time
from PIL import Image
import pytesseract
import csv
import subprocess 
app_path = r'C:\Users\sdsow\OneDrive\Desktop\LDPlayer9.lnk'
subprocess.run(app_path,shell='True')

time.sleep(5)





x=740
y=296
time.sleep(10)

pyautogui.click(x, y)
#clicks Kite app
x=1613
y=181
time.sleep(10)
pyautogui.click(x, y)

#clicks demo
x=952
y=927
time.sleep(5)
pyautogui.click(x, y)
time.sleep(2)
for a in range(10):
    
    pyautogui.press('fn')
    pyautogui.press('f11')
    def take_screenshot():
        time.sleep(2)
        screenshot = pyautogui.screenshot()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"C:\Users\Blaze\Desktop\sample\images1\{timestamp}.png"
        
        screenshot.save(screenshot_path)
        return screenshot_path
    screenshot_path = take_screenshot()     
    time.sleep(2)
    pyautogui.press('fn')
    pyautogui.press('f11')
    time.sleep(5)