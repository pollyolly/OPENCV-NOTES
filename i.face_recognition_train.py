import cv2 as cv
import numpy as np
import os

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
dir = r'images/train'

haar_cascade = cv.CascadeClassifier('data/haarcascade_frontalcatface_extended.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(dir, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f'Lenght of the features = {len(features)}')
print(f'Lenght of the labels = {len(labels)}')

print('Training done --------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

#pip install opencv-contrib-python
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train Recognizer on the Features list and Labels list
face_recognizer.train(features, labels)
# Save Trained data
# Generated Trained data
face_recognizer.save('data/face_trained.yml')
np.save('face_recognition_features.npy', features)
np.save('face_recognition_labels.npy', labels)