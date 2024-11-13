import cv2
import numpy as np
import matplotlib.pyplot as plt

#handle images
clrimg = cv2.imread("clr.png",cv2.IMREAD_COLOR)
bwimg = cv2.imread("bw.png",cv2.IMREAD_GRAYSCALE)

B, G, R = cv2.split(clrimg) 
cv2.imshow("original", clrimg) 
cv2.imshow("blue", B) 
cv2.imshow("Green", G) 
cv2.imshow("red", R) 
cv2.waitKey(0) 
  
cv2.destroyAllWindows() 