import cv2
import numpy as np
import matplotlib.pyplot as plt

#handle images
bkh = cv2.imread("clr.png",cv2.IMREAD_COLOR)
print(bkh.shape)
shrunk = cv2.resize(bkh, (0, 0), fx = 0.05, fy = 0.05)
stretched = cv2.resize(bkh, (2048,2048))#width, height

#interpolations
linear_interpolated = cv2.resize(bkh, (2048,2048),interpolation = cv2.INTER_LINEAR)
exact_interpolated = cv2.resize(bkh, (2048,2048),interpolation = cv2.INTER_LINEAR_EXACT)
area_interpolated = cv2.resize(bkh, (2048,2048),interpolation = cv2.INTER_AREA)
tabsize2_interpolated = cv2.resize(bkh, (2048,2048),interpolation = cv2.INTER_NEAREST)
nearest_interpolated = cv2.resize(bkh, (2048,2048),interpolation = cv2.INTER_CUBIC)
lanxzs04_interpolated = cv2.resize(bkh, (2048,2048),interpolation = cv2.INTER_LANCZOS4)

Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[bkh, shrunk, stretched, linear_interpolated]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()

cv2.imshow("Linear Interpolated", linear_interpolated)
cv2.imshow("Exact Interpolated", exact_interpolated)
cv2.imshow("Area Interpolated", area_interpolated)
cv2.imshow("Tabsize2 Interpolated", tabsize2_interpolated)
cv2.imshow("Nearest Interpolated", nearest_interpolated)
cv2.imshow("Lanczos4 Interpolated", lanxzs04_interpolated)

cv2.waitKey(0)

