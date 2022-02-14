import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Task1.1
img = cv.imread("pic4.jpg")
fig, ax = plt.subplots(ncols=4, nrows=2, figsize=(20, 5))

ax[0, 0].imshow(img)
ax[0, 0].set_title("BGR")

ax[0, 1].imshow(img[:, :, 0], cmap="gray")  
ax[0, 1].set_title("B")

ax[0, 2].imshow(img[:, :, 1], cmap="gray")
ax[0, 2].set_title("G")

ax[0, 3].imshow(img[:, :, 2], cmap="gray")
ax[0, 3].set_title("R")

new_img = img[:, :, ::-1]
ax[1, 0].imshow(new_img)
ax[1, 0].set_title("RGB")

ax[1, 1].imshow(new_img[:, :, 0], cmap="gray")
ax[1, 1].set_title("R")

ax[1, 2].imshow(new_img[:, :, 1], cmap ="gray")
ax[1, 2].set_title("G")

ax[1, 3].imshow(new_img[:, :, 2], cmap="gray")
ax[1, 3].set_title("B")

plt.show()