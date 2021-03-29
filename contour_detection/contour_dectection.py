import cv2
img = cv2.imread('bird.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def resize_image(img, scale = 0.3):
    height, width = img.shape[:2]
    height = int(height * scale)
    width = int(width * scale)
    return cv2.resize(img, (width, height))

img = resize_image(img)
cv2.imshow('bird', img)

img_blur =  cv2.GaussianBlur(img, (3,3), 0)
canny = cv2.Canny(img, 125, 175)
contours, hierarchies = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
# cv2.imshow('canny', canny)
# cv2.imshow('blur', img_blur)

cv2.waitKey(0)
