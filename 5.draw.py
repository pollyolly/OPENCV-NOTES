import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

#1. Paint the image a certain color
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

#2. Draw Rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

#3. Draw Rectangle based on window Shape
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

#4. Draw Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

#5. Draw line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

#6. Put Text
cv.putText(blank, 'Hello World', (125,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)