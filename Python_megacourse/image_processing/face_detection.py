import cv2

# https://github.com/opencv/opencv/tree/master/data/haarcascades

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("my_pic.jpeg")

gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

print(faces)
print(type(faces))

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(244,134,66),3)

resized=cv2.resize(img,((int(img.shape[1]/2)),int(img.shape[0]/2)))
cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

