import cv2 #this is for the import of open cv

framewidth = 640
framehieght = 360

cap = cv2.VideoCapture(0)

while True:
    sucess, img = cap.read()
    cv2.imshow('vidow', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
