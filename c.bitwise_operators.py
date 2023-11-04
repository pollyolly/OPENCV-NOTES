import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)
#Bitwise And
bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow('Bitwise And', bitwise_and)
#Bitwise Or
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise Or', bitwise_or)
#Bitwise Xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise Xor', bitwise_xor)
#Bitwise Not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise Not', bitwise_not)

cv.waitKey(0)