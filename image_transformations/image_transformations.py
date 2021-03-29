import cv2
import numpy as np
class ImageTransformations():
    def __init__(self, image_path):
        self.img = cv2.imread(image_path)

    def translation(self, x, y):
        # -x --> left
        # +x --> right
        # -y --> up
        # +y --> down
        translationMatrix = np.float32([[1,0,x],[0,1,y]])
        dimensions = (self.img.shape[1], self.img.shape[0])
        self.img_out = cv2.warpAffine(self.img, translationMatrix, dimensions)

    def rotation(self, angle):
        height, width = self.img.shape[:2]
        # Rotation point
        mid_point = (height//2, width//2)
        rot_mat = cv2.getRotationMatrix2D(mid_point, angle, 1)
        self.img_out = cv2.warpAffine(self.img, rot_mat, (width, height))

    def flipping(self, type_flip):
        """
        type_flip:
        0 - xoay ngang
        1 - xoay doc
        -1 - xoay ca ngang lan doc
        """
        self.img_out = cv2.flip(self.img, type_flip)

if __name__ == "__main__":
    it = ImageTransformations('test.jpg')
    cv2.imshow('original', it.img)

    it.translation(100, 100)
    cv2.imshow('translation', it.img_out)

    it.rotation(45)
    cv2.imshow('rotation', it.img_out)

    it.flipping(-1)
    cv2.imshow('flipping', it.img_out)
    cv2.waitKey(0)