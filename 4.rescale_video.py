import cv2 as cv

capture = cv.VideoCapture('videos/place_video.mp4')

# Existing Images, Video and Live Video Rescaling
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Live Video Rescaling
def changeRes(width, height):
    capture.set(3, width)
    capture.set(1, height)

#Read video frames
while True:
    isTrue, frame = capture.read()
    resizedFrame = rescaleFrame(frame)
    cv.imshow('Video', resizedFrame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

#video will stop after all frames are looped
#it will output a path error
#since frames are like images