import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# 1. BGR to Grayscale -----
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. BGR to HSV ------
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# 3. BGR to LAB --
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# 4. BGR to RGB -------
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# 5. HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)
