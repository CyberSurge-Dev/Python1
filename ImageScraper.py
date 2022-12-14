import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt

IMAGE_PATH = 'Image_source\Capture.PNG'


reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH, paragraph="False")

print(result)
