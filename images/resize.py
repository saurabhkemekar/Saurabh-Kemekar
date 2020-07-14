import cv2
import numpy as np


str = "graphic-design-4.jpg"

img = cv2.imread(str)

img = cv2.resize(img, (1600,623) ,  interpolation = cv2.INTER_CUBIC)

cv2.imwrite(str,img)

cv2.destoryAllWindows()
