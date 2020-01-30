import cv2

#create the haar cascade ---- creating the classifier
clasi = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# import the image
image = cv2.imread("housefull.jpg",1)
i=1
r_image = cv2.resize(image,(int(image.shape[1]/i),int(image.shape[0]/i)))

#Detecting the faces in the image
face= clasi.detectMultiScale(
    r_image,
    scaleFactor=1.3,
    minNeighbors=2)

# printing that face is found
print("Pooja is detected {0}".format(len(face)))
print(type(face))
print(face)


# drawing a rectangle
for (x,y,w,h) in face :
    cv2.rectangle(r_image,(x,y),(x+w,y+h),(100,10,255),2)


#Displaying
cv2.imshow("Pooja Hegde",r_image)
cv2.waitKey(0)

