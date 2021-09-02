import cv2
import numpy as np

def nothing(x):
    pass

#cap = cv2.VideoCapture('imagens/carros.mp4');

cv2.namedWindow("Tracking")
cv2.createTrackbar("LB", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LG", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LR", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UB", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UG", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UR", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('imagens/Carros.jpg')
    #_, frame = cap.read()

    
    l_h = cv2.getTrackbarPos("LB", "Tracking")
    l_s = cv2.getTrackbarPos("LG", "Tracking")
    l_v = cv2.getTrackbarPos("LR", "Tracking")

    u_h = cv2.getTrackbarPos("UB", "Tracking")
    u_s = cv2.getTrackbarPos("UG", "Tracking")
    u_v = cv2.getTrackbarPos("UR", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(frame, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break
        
    

cap.release()
cv2.destroyAllWindows()