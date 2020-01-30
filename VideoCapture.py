import cv2,time

classi = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video=cv2.VideoCapture(0)

i=1

while True :
    i += 1
    check,frame = video.read()
    print(frame)

    #face detection
    face =classi.detectMultiScale(frame,scaleFactor=1.3,minNeighbors=4)

    
    #drawing the rectangle
    for x,y,w,h in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,10,255),2)


    # display the image
    cv2.imshow("Image",frame)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(i)
video.release()