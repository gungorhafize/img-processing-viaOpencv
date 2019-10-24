import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('color.png',1)
b,g,r = cv2.split(img)
cv2.imshow('Blue Channel',b)
cv2.imshow('Green Channel',g)
cv2.imshow('Red Channel',r)
img=cv2.merge((b,g,r))
cv2.imshow('Merged Output',img)

cv2.waitKey(0)
cv2.destroyAllWindows()