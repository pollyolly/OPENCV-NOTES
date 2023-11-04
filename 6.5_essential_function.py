import cv2 as cv

img = cv.imread('images/hot_air_balloon.jpg')
# cv.imshow('Boston', img)

#1. Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#2. Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#3. Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edge', canny)

#4. Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#5. Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#6. Resize
resized = cv.resize(img, (100,100), interpolation=cv.INTER_AREA)
cv.imshow('Resize', resized)

#7. Cropped
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)