import cv2 as cv

img = cv.imread('images/people_group.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

#haarcascade_frontalcatface_extended
#Downloaded From
#https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalcatface_extended.xml

haar_cascade = cv.CascadeClassifier('data/haarcascade_frontalcatface_extended.xml')
#Get Detected Faces
#Note: Can only detect in Center Part
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

#Draw Rectangle on Faces
for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow('Faces Detected', img)

cv.waitKey(0)
#Not recommended for production use