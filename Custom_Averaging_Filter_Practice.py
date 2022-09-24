import cv2
import numpy as np

img = cv2.imread("C:\\Users\\bareera\\Documents\\virtualen\\CV\\mountains.jpg")

kernel = np.ones((3,3), np.float32)/9
newimg = cv2.filter2D(img, -1, kernel)


cv2.imshow("Averaged Image", np.hstack((img, newimg)))



# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()
