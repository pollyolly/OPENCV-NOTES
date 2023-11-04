import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('data/haarcascade_frontalcatface_extended.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# feature = np.load('face_recognition_features.npy', allow_pickle=True)
# labels = np.load('face_recognition_labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('data/face_trained.yml')

img = cv.imread('images/val/ben_afflek/3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
