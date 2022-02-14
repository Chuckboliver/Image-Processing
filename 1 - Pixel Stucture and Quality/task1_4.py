import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2 as cv

img = cv.imread("pic4.jpg") 
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.resize(img, (90, 160), interpolation=cv.INTER_AREA)


xx, yy = np.mgrid[0:img.shape[0], 0:img.shape[1]]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, img ,rstride=1, cstride=1, cmap=plt.cm.gray,
        linewidth=0)

plt.show()
