import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 500, 240)

trackbar = cv2.createTrackbar("hue min", "TrackBars", 79, 179, empty)
trackbar = cv2.createTrackbar("hue max", "TrackBars", 140, 179, empty)
trackbar = cv2.createTrackbar("sat min", "TrackBars", 10, 255, empty)
trackbar = cv2.createTrackbar("sat max", "TrackBars", 255, 255, empty)
trackbar = cv2.createTrackbar("value min", "TrackBars", 27, 255, empty)
trackbar = cv2.createTrackbar("value max", "TrackBars", 220, 255, empty)

while True:
    img = cv2.imread("sh.png")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hue_min = cv2.getTrackbarPos("hue min", "TrackBars")
    hue_max = cv2.getTrackbarPos("hue max", "TrackBars")
    sat_min = cv2.getTrackbarPos("sat min", "TrackBars")
    sat_max = cv2.getTrackbarPos("sat max", "TrackBars")
    val_min = cv2.getTrackbarPos("value min", "TrackBars")
    val_max = cv2.getTrackbarPos("value max", "TrackBars")
    
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    segment = cv2.inRange(imgHSV, lower, upper)
    img_seg = cv2.bitwise_and(img, img, mask=segment)

    cv2.imshow('TrackBars', img_seg)
    # cv2.imshow('shoe', imgHSV)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break