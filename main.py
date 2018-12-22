#coding:utf-8
import numpy as numpy
import cv2

capture = cv2.VideoCapture(0) # Capture your primary webcam

while True: #infinite loop
	ret, frame = capture.read() # reading frame by frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # capturing grayscale video
	cv2.imshow('frame', frame) #imgshow
	cv2.imshow('gray', gray) # loading grayscale
	if cv2.waitKey(30) & 0xff == ord('q'): # type "q" to stop the program
		break

capture.release() # release the capture
cv2.destroyAllWindows()
