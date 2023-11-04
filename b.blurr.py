import cv2 as cv
import numpy as np

img = cv.imread('images/hot_air_balloon.jpg')
cv.imshow('Hot Air Balloon', img)
#Average Blur
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)
#Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)
#Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)
#Bilateral
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)