import cv2
import numpy as np
import matplotlib.pyplot as plt

#handle images
bkh = cv2.imread("clr.png",cv2.IMREAD_COLOR)
neil = cv2.imread("neil.png",cv2.IMREAD_COLOR)

sumof = cv2.addWeighted(bkh, 1, neil, 0.3, 0) 
cv2.imshow('SUM Image', sumof) 

diffof = cv2.subtract(bkh,neil)
cv2.imshow('Difference Image', diffof)

orof = cv2.bitwise_or(bkh,neil)
cv2.imshow('OR Image', orof)

xorof = cv2.bitwise_xor(bkh,neil)
cv2.imshow('XOR Image', xorof)


andof = cv2.bitwise_and(bkh,neil)
cv2.imshow('AND Image', andof)


notof = cv2.bitwise_not(bkh,neil)
cv2.imshow('NOT Image', notof)

# #increased info, rudiemntary enchancement
# sumof1 = cv2.addWeighted(bkh, 1, bkh, 10, 0)
# og = cv2.imshow('Original Image', bkh) 
# cv2.imshow('Weighted2 Image', sumof1) 








cv2.waitKey(0)
cv2.destroyAllWindows
