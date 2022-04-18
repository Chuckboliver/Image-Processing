import cv2 as cv
import numpy as np

img = cv.imread("pic4.jpg")
print(img.shape)

new_image = np.transpose(img, (2, 0, 1))
print(new_image.shape)