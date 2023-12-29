import pyautogui
import time
from PIL import Image
import pytesseract
import csv
import subprocess
app_path = r'C:\Users\Blaze\Desktop\LDMultiPlayer.lnk'
subprocess.run(app_path,shell='True')
x=893
y=249
counter = 1
count =10
time.sleep(7)

pyautogui.click(x, y)

#Clicks start dummy-1

x=680
y=198
time.sleep(25)

pyautogui.click(x, y)
#clicks Kite app
x=607
y=587
time.sleep(10)
pyautogui.click(x, y)
#clicks demo
time.sleep(2)
pyautogui.press('f11')

scroll_progress = 0  # Variable to track the scrolling progress

while scroll_progress < 7:
    def take_screenshot():
        time.sleep(2)
        screenshot = pyautogui.screenshot()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"C:/Users/Blaze/Desktop/sample/images/{timestamp}.png"
        screenshot.save(screenshot_path)
        return screenshot_path

    screenshot_path = take_screenshot()

    # Path to the Tesseract executable (change this to the path on your machine)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def image_to_text(image_path):
        # Open the image file
        img = Image.open(image_path)

        # Convert the image to grayscale
        img_gray = img.convert('L')

        # Use Tesseract OCR to extract text
        text = pytesseract.image_to_string(img_gray)

        return text

    def save_to_csv(image_path):
          # Use the nonlocal keyword to reference the outer counter variable
        global counter
       
          
        csv_file = f'C:/Users/Blaze/Desktop/sample/zerodha/outputdata_{counter}.csv'

        counter +=1

        # Extract text from the specified image
        extracted_text = image_to_text(image_path)

        # Split the extracted text into lines
        lines = extracted_text.split('\n')

        # Extracting name and values from the lines
        data_list = []
        for line in lines:
            if line.strip():  # Ignore empty lines
                parts = line.split()
                if len(parts) >= 2:
                    name = parts[0]
                    value = ' '.join(parts[1:])
                    data_list.append({'Stock': name, 'Percentage': value})

        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Stock', 'Percentage']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header row
            writer.writeheader()

            # Write data to CSV
            writer.writerows(data_list)

    # Use the screenshot taken in the code
    save_to_csv(screenshot_path)
    pyautogui.scroll(-1000)  # Adjust the scroll value based on your requirement
    time.sleep(2)  # Adjust the sleep duration based on your requirement
    scroll_progress += 1
pyautogui.press('f11')
app_path = r'C:\LDPlayer\ldmutiplayer\dnmultiplayerex.exe'

subprocess.run(app_path,shell='True')
x=905
y=302
time.sleep(5)
pyautogui.click(x, y)
#starts dummy 2

x=695
y=229
time.sleep(30)
pyautogui.click(x, y)
#clicks kite app
x=692
y=649
time.sleep(10)
pyautogui.click(x, y)
#clicks demo
time.sleep(2)
pyautogui.press('f11')

scroll_progress = 0  # Variable to track the scrolling progress

while scroll_progress < 7:
    def take_screenshot():
        time.sleep(5)
        screenshot = pyautogui.screenshot()
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"C:/Users/Blaze/Desktop/sample/images/{timestamp}.png"
        screenshot.save(screenshot_path)
        return screenshot_path

    screenshot_path = take_screenshot()

    # Path to the Tesseract executable (change this to the path on your machine)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def image_to_text(image_path):
        # Open the image file
        img = Image.open(image_path)

        # Convert the image to grayscale
        img_gray = img.convert('L')

        # Use Tesseract OCR to extract text
        text = pytesseract.image_to_string(img_gray)

        return text

    def save_to_csv(image_path):
          # Use the nonlocal keyword to reference the outer counter variable
        global count
       
        csv_file = f'C:/Users/Blaze/Desktop/sample/zerodha/outputdata_{count}.csv'

        count +=1

        # Extract text from the specified image
        extracted_text = image_to_text(image_path)

        # Split the extracted text into lines
        lines = extracted_text.split('\n')

        # Extracting name and values from the lines
        data_list = []
        for line in lines:
            if line.strip():  # Ignore empty lines
                parts = line.split()
                if len(parts) >= 2:
                    name = parts[0]
                    value = ' '.join(parts[1:])
                    data_list.append({'Stock': name, 'Percentage': value})

        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Stock', 'Percentage']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header row
            writer.writeheader()

            # Write data to CSV
            writer.writerows(data_list)

    # Use the screenshot taken in the code
    save_to_csv(screenshot_path)
    pyautogui.scroll(-1000)  # Adjust the scroll value based on your requirement
    time.sleep(2)  # Adjust the sleep duration based on your requirement
    scroll_progress += 1
pyautogui.press('f11')




