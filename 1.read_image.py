import cv2 as cv

img = cv.imread('images/hot_air_balloon.jpg')

cv.imshow('Balloon', img)

cv.waitKey(0)

