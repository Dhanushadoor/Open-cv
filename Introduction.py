import cv2
img = cv2.imread("poja.jpg",1)
print(img.shape)
# cv2.imshow("Dhanush",img)
res = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Dhanushhhhhhhhhh",res)
cv2.waitKey(0)
cv2.destroyAllWindows()