import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# 01:32:30
cv.waitKey(0)
