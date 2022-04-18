import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

S_MAX = 255
S_MIN = 0

def calculate_q(Si, q_level):
    a = (Si - S_MIN) / (S_MAX - S_MIN)
    q = math.floor(a * q_level)
    return q        

def reduce_bit_depth(img, bit_depth):
    q_level = 2 ** bit_depth
    height, width = img.shape
    result_img = np.zeros(shape=(height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            q = calculate_q(img[i, j], q_level)
            result_img[i, j] = q
    return result_img


    
img = cv.imread("pic4.jpg")

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

new_img = reduce_bit_depth(img, 2)
fig, ax = plt.subplots(ncols=2, nrows=1, figsize=(20, 10))
ax[0].imshow(img, cmap="gray")
ax[0].set_title("Bit depth 8")
ax[1].imshow(new_img, cmap="gray")
ax[1].set_title("Bit depth 2")
plt.show()