import cv2

img = cv2.imread('Pictures/Weimaraner/2.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()