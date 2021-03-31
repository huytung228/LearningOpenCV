import cv2
import numpy as np
img = cv2.imread('scan.jpg')

def empty(a):
    pass

def resize_img(img, scale = 0.3):
    height, width = img.shape[:2]
    height = int(height * scale)
    width = int(width * scale)
    return cv2.resize(img, (width, height))

img = resize_img(img)

img = cv2.GaussianBlur(img,(5,5),0)

# Using track bar for get suitable value for canny
# cv2.namedWindow("doc")
# trackbar = cv2.createTrackbar("min threadsold", "doc", 100, 1000, empty)
# trackbar = cv2.createTrackbar("max threadsold", "doc", 458, 1000, empty)

# while True:
#     min_th = cv2.getTrackbarPos("min threadsold", "doc")
#     max_th = cv2.getTrackbarPos("max threadsold", "doc")

#     canny_img = cv2.Canny(img,min_th,max_th)

#     cv2.imshow('doc', canny_img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         exit()


# After using trackbar chose value for canny is min:138 max:735
canny_img = cv2.Canny(img,100,458)

kernel = np.ones((5,5),np.uint8)
dilate_img = cv2.dilate(canny_img,kernel,iterations = 1)

# get contours
contours, hierarchies = cv2.findContours(dilate_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# get contour areas
area_contours = [cv2.contourArea(cnt) for cnt in contours]

# find the biggest area contour
biggest_area_index = np.argmax(area_contours)
cnt = contours[biggest_area_index]

cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
print(cnt)

cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)


cv2.imshow('doc', img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    exit()

