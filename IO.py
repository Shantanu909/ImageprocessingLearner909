import cv2
import numpy as np
import matplotlib.pyplot as plt

#handle images
clrimg = cv2.imread("clr.png",cv2.IMREAD_COLOR)
bwimg = cv2.imread("bw.png",cv2.IMREAD_GRAYSCALE)

nameclr = "Colour Image"
namebw= "BW Image"

cv2.imshow(nameclr,clrimg)
cv2.imshow(namebw,bwimg)

#BGR Faulted
plt.imshow(clrimg)
plt.show()

#RGB Corrected
clrcrctd = cv2.cvtColor(clrimg,cv2.COLOR_BGR2RGB)
plt.imshow(clrcrctd)

#image write

filename = "clr_corrected.tiff"
cv2.imwrite(filename,clrcrctd)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
#image info
print(clrimg.shape)
print(clrimg.size)
print(clrimg.dtype)

print(bwimg.shape)
print(bwimg.size)
print(bwimg.dtype)
