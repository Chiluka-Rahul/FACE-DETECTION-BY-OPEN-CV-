import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

while True:

	_,img=cap.read()

	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	face=face_cascade.detectMultiScale(gray,2,2)

	for (a,b,x,y) in face:

		cv2.rectangle(img,(a,b),(a+x,b+y),(255,0,0),2)

	cv2.imshow('img',img)
	
	k=cv2.waitKey(30) & 0xff

	if k==27:
	
		break

cv2.release()