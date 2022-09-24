import cv2
import numpy

img = cv2.imread("mountains.jpg")

newimg = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow("After applying Gaussian Blur", numpy.hstack((img,newimg)))

cv2.waitKey(0)
cv2.destroyAllWindows