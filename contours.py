import cv2 as cv
import numpy as mp
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
#
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# contours = a list of all the coordinates
# hierarchies = the representations of the contours
# RETR_LIST = return all the contours they find in the image (THERE MORE TYPE THAN 'LIST')
# CHAIN_APPROX_NONE = return all of the contours (*_SIMPLE - compress all the points)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
