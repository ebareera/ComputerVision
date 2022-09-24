import cv2
import numpy

img = cv2.imread("mountains.jpg")

newimg = cv2.blur(img, (3,3))
cv2.imshow("Blurred Image", numpy.hstack((img, newimg)))

cv2.waitKey(0)
cv2.destroyAllWindows()