import os

from PIL import Image
from pytesseract import pytesseract

# Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Define path to images folder
path_to_images = r'images/'

# Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):

    # Iterate over each file name in the folder
    for file_name in file_names:

        # Open image with PIL
        img = Image.open(path_to_images + file_name)

        # Extract text from image
        text = pytesseract.image_to_string(img)

        # Print text of every image
        print(text)
