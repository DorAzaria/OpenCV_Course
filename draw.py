import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# 1. Paint the image
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green',blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)  # or thickness = cv.FILLED

# 3. Draw a circle
cv.circle(blank, (250,250), 40,(0,0,255),thickness=-1)

# 4. Draw a line
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)

# 5. Draw a text
cv.putText(blank,'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,180,50), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)
