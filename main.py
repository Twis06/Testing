import cv2

cap = cv2.VideoCapture("app.mp4")

ret, frame = cap.read()

cv2.imshow("Img", frame)
cv2.waitKey(0)