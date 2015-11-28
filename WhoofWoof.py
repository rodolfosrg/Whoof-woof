import cv2
import numpy as np

def Otsu(img):
	gblur = cv2.GaussianBlur(img,(5,5),0)
	ret,otsu = cv2.threshold(gblur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return otsu

def Laplacian(img):
	gblur = cv2.GaussianBlur(img,(5,5),0)
	laplacian = cv2.Laplacian(gblur, cv2.CV_64F);	
	return laplacian

img = cv2.imread('Pictures/Weimaraner/2.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Pictures/Weimaraner/3.jpg',cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('Pictures/Weimaraner/4.jpg',cv2.IMREAD_GRAYSCALE)
ret,binary = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)
kernel = np.ones((3,3),np.float32)/9
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(8,8))


cv2.imshow('1',Laplacian(img))
cv2.imshow('2',Laplacian(img2))
cv2.imshow('3',Laplacian(img3))

cv2.waitKey(0)
cv2.destroyAllWindows()