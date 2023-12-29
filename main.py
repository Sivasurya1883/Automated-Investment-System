import os
import time
from PIL import Image
import pytesseract
import re
from datetime import datetime
import mysql.connector

# Set the path to Tesseract executable (change this path based on your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to the folder containing images
folder_path = r"C:\Users\Blaze\Desktop\sample\images1"

# Coordinates for the region in the image (adjust these according to your image)
specified_region_coordinates = (0, 0, 1050, 1050)  # Example coordinates

# MySQL database configuration
db_config = {
    'host': '178.63.152.236',
    'user': 'blaze',
    'password': 'blaze.ws',
    'database': 'Delete_img'
}

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

def extract_value_from_image(image):
    # Use pytesseract to extract text from the specified region in the image
    cropped_img = image.crop(specified_region_coordinates)
    text = pytesseract.image_to_string(cropped_img)

    # Find the P&L value in the extracted text using regex
    matches = re.findall(r'[-+]?\b\d{1,3}(?:,\d{3})*\.\d{2}\b', text)
    if matches:
        pnl_value = matches[0].replace(",", "")  # Remove commas
        return pnl_value
    return None

def get_image_modified_time(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return None

    # Get the modification time of the image file
    modified_time = os.path.getmtime(file_path)
    modified_time_str = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
    return modified_time_str

def delete_processed_image(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    except OSError as e:
        print(f"Error deleting the file {file_path}: {e}")

def get_processed_files_from_db():
    try:
        cursor.execute("SELECT filename FROM delete_images")
        rows = cursor.fetchall()
        processed_files = set(row[0] for row in rows)
        return processed_files
    except mysql.connector.Error as err:
        print(f"Error fetching processed files from MySQL: {err}")
        return set()

def process_new_images():
    while True:
        processed_files = get_processed_files_from_db()
        # Iterate through files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if the file is an image and not already processed
            if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.avif')):
                if filename not in processed_files:
                    # Open the image
                    img = Image.open(file_path)

                    # Get image modification time
                    modified_time = get_image_modified_time(file_path)

                    # Extract P&L value from the image
                    pnl_value = extract_value_from_image(img)

                    if pnl_value:
                        print(f"File: {filename}, Modified Time: {modified_time}, P&L Value: {pnl_value}")

                        # Insert data into MySQL database
                        try:
                            insert_query = "INSERT INTO delete_images (filename, modified_time, pnl_value) VALUES (%s, %s, %s)"
                            cursor.execute(insert_query, (filename, modified_time, pnl_value))
                            conn.commit()
                        except mysql.connector.Error as err:
                            print(f"Error inserting data into MySQL: {err}")
                        else:
                            # Delete the processed file
                            delete_processed_image(file_path)

        # Wait for 10 seconds before checking for new files again
        time.sleep(10)  # 10 seconds

# Start monitoring for new images in the folder
process_new_images()