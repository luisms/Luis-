




import cv2
import sys

# Get user supplied values



# Create the haar cascade
faceCascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalcatface.xml')

# Read the image
image = cv2.imread('/home/pi/tfg/fotos/3.jpg')
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = image
cv2.imshow("",gray)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.35 ,
    minNeighbors=6,
    minSize=(100, 100),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print ("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

#cv2.imshow("Faces found", image)
#cv2.waitKey(0)
cv2.imwrite("test.jpg",image)
