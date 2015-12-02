import cv2, os
import numpy as np
from subprocess import call

breeds = os.listdir("Pictures")

cascade = cv2.CascadeClassifier('Pictures/Beagle/cascade.xml')
img = cv2.imread("Test/beagle.jpg",cv2.IMREAD_GRAYSCALE)
print cascade.detectMultiScale(img, 1.3, 5)