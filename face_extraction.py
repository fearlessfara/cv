#	Name        : face_extraction.py
#	Author      : Faraone Christian Gennaro
#	Version     : 1.0
#	Copyright   : GNU GPL License (do whatever you want)
#	Description : Simple face extractor from pictures


#	ATTENTION
#	this script was firstly ideated to retrieve the biggest face on a resume (usually the only and biggest face 
#	on a resume shoule be of the candidate). We're using an intel premade xml cascade (it's a no deal training
#	a new one just for recognizing faces in an easy environment)


#
#	we'll need only those two external libraries, this is a pretty light and vanilla project
import cv2
import base64


def face_finder(cv_path):
	face_cascade = cv2.CascadeClassifier('face_detection.xml')

	img = cv2.imread(cv_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	#take only the first result (biggest face on the pic)
	face = faces[0]

	x = face[0]
	y = face[1]
	w =face[2]
	h = face[3]


	crop_img = img[(y-15):y+(h+15), (x-15):x+(w+15)]
	width = 200
	height = 200
	dim = (width, height)
	# resize image to a fixed size 200x200
	# we used to resize the image because storing an heavy blob on a DB is pretty uncomfortable
	resized = cv2.resize(crop_img, dim, interpolation = cv2.INTER_LINEAR)
 

	# cv2.imwrite("name.jpg", resized)
	retval, buffer = cv2.imencode('.jpg', crop_img)

	img_base64 = base64.b64encode(buffer)

	return img_base64
