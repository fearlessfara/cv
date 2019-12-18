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
	resized = cv2.resize(crop_img, dim, interpolation = cv2.INTER_LINEAR)
 

	# cv2.imwrite("name.jpg", resized)
	retval, buffer = cv2.imencode('.jpg', crop_img)

	img_base64 = base64.b64encode(buffer)


	return img_base64
