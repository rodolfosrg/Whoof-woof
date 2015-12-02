import cv2, os
from subprocess import call

breeds = os.listdir("Pictures")
breeds = ['Beagle']
# Create training vectors for each breed
for breed in breeds:
	call(["opencv_createsamples", \
		"-info",breed.lower()+"-positive.txt", \
		"-bg","negatives.txt", \
		"-vec",breed.lower()+"-vector.vec"])
	call(["opencv_traincascade", \
		"-vec",breed.lower()+"-vector.vec", \
		"-bg","negatives.txt", \
		"-data","Pictures/" + breed, \
		"-numPos","12", \
		"-numNeg","3045", \
		"-numStages","6", \
		"mode","ALL"])