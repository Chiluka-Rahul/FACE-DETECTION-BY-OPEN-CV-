import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('photo.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray,2,2)

for (a,b,x,y) in face:

	cv2.rectangle(img,(a,b),(a+x,b+y),(255,0,0),2)

cv2.imshow('img',img)

cv2.waitKey()