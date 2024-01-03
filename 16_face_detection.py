# Project 16
# Python Face Detection

#1. Go to the terminal and paste this command 'pip install opencv-python'
#2. Add this file named 'haarcascade_frontalface_default.xml' (available in github repository) into the file in which you are storing this python project
#3. Take a photo of yours, add to this file and rename it 'test' so 'test.png' or 'test.jpg' check accordingly

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (225, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()

cv2.imwrite("face_detected.jpg", img)
