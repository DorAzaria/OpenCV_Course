import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# 2. Blur the image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# 3. Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# 4. Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilate', dilated)

# 5. Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroding', eroded)

# 6. Resize
resize = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resize', resize)

# 7.Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
