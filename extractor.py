import cv2
import pytesseract
import re
import json
import numpy as np

# load the image using OpenCV
image = cv2.imread("/Users/gunjan/Downloads/PXL_20240913_170153148.jpg")

# convert the image to grayscale for better OCR results
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# tesseract to extract text from the image
text = pytesseract.image_to_string(gray)
# # print(text)
#
# convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# applying OCR using tesseract
text = pytesseract.image_to_string(gray)

# list of names
target_names = ["Gunjan"]

# regular expression to extract target_names

# pattern that looks for any name in the target_names list
name_pattern = r'\b(?:' + '|'.join(target_names) + r')\b'
matches = re.findall(name_pattern, text)

print("Extracted names:", matches)
