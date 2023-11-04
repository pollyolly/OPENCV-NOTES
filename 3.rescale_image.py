import cv2 as cv

img = cv.imread('images/hot_air_balloon.jpg')

cv.imshow('Balloon', img)

def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)