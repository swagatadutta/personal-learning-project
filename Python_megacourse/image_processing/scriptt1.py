import cv2

img=cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img.shape)
print(img)
resized_img=cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
#resized_img=cv2.resize(img, (400,700))
cv2.imshow("galaxy", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("galaxy_resized.jpg", resized_img)
