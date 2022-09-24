import cv2
import numpy

img = cv2.imread("rose.jpg")
newimg = cv2.medianBlur(img, 3)

cv2.imshow("After applying median Blur", numpy.hstack((img,newimg)))

cv2.waitKey(0)
cv2.destroyAllWindows()