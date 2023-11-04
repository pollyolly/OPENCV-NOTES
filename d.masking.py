import cv2 as cv
import numpy as np

img = cv.imread('images/hot_air_balloon.jpg')
cv.imshow('Hot Air Balloon', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)