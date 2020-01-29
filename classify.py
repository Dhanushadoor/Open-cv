import cv2

#create the classifier object
clasi = cv2.CascadeClassifier("F:\\openCVTest\\haarcascade_frontalface_default.xml")


#read the image

img1 = cv2.imread("poja.jpg")
r_img = cv2.resize(img1,(int(img1.shape[1]/2),int(img1.shape[0]/2)))    

#reading the image as gray scale image
g_img = cv2.cvtColor(r_img,cv2.COLOR_BGR2GRAY)  


#search the coordinates of the image
face = clasi.detectMultiScale(g_img,scaleFactor=1.05,minNeighbors=5)

print(type(face))

print(face)

cv2.imshow("Poja hegde",g_img)
cv2.waitKey(0)




