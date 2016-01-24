"""
precesa todos los archivos .jpg de un directorio y
escribe el resultado con el nobre imagen + var + .jpg
"""
import cv2
import sys
import glob

# Get user supplied values
nombres = glob.glob("*.jpg")
print (nombres)
def trabajo( nombres):
    faceCascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalcatface.xml')
# Create the haar cascade
    a = 1

    for i in nombres:
        aux = a
        num = str (aux)
        salida =("imagen"+num+".jpg")
        print(salida)
        ruta = '/home/pi/tfg/fotos/'+i
        # Read the image
        image = cv2.imread(ruta)
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = image
        #cv2.imshow("",gray)
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1 ,
            minNeighbors=3,
            minSize=(5, 5),
            flags = cv2.CASCADE_SCALE_IMAGE
        )

        print ("Found {0} faces!".format(len(faces)))

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #cv2.imshow("Faces found", image)
        #cv2.waitKey(0)
        cv2.imwrite(salida, image)
        a=a+1



trabajo(nombres)
