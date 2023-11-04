import cv2 as cv

capture = cv.VideoCapture('videos/place_video.mp4')

#Read video frames
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

#video will stop after all frames are looped
#it will output a path error
#since frames are like images