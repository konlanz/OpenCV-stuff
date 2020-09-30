import cv2

path = "resource/Lena.png"

img = cv2.imread(path)
print(img.shape)

width, hieght = 600, 400
cv2.imshow('road', img)

imgResize = cv2.resize(img, (width, hieght))
cv2.imshow('lena', imgResize)

cv2.waitKey(0)
