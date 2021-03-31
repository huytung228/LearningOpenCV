import cv2
import numpy as np

img = cv2.imread('shape.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def empty(a):
    pass

cv2.namedWindow("binary")
trackbar = cv2.createTrackbar("min threadsold", "binary", 70, 255, empty)
trackbar = cv2.createTrackbar("max threadsold", "binary", 255, 255, empty)

# def resize_image(img, scale = 0.3):
#     height, width = img.shape[:2]
#     height = int(height * scale)
#     width = int(width * scale)
#     return cv2.resize(img, (width, height))

# img = resize_image(img, 1)

min_th = cv2.getTrackbarPos("min threadsold", "binary")
max_th = cv2.getTrackbarPos("max threadsold", "binary")

_, imgBinary = cv2.threshold(imgGray,min_th,max_th,cv2.THRESH_BINARY)

img_blur =  cv2.GaussianBlur(imgBinary, (3,3), 0)

contours, hierarchies = cv2.findContours(img_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 5)

x,y,w,h = cv2.boundingRect(contours[0])
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(0,0,255),2)


cv2.imshow('binary', img)

if cv2.waitKey(0) & 0xFF == ord('q'):
   exit()
