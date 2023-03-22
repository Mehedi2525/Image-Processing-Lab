import math
import matplotlib.pyplot as plt
import cv2
import numpy as np


'''
Image input and converting as gray
'''
rgb_img = plt.imread('einstein.jpg')
# print(rgb_img)

# Gray
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)

'''Histogram equilization'''


hight, width = gray_img.shape






hist = []


for k in range(256):
    count = 0
    for i in range(hight):
        for j in range(width):
            if gray_img[i][j] == k:
                count = count+1
    hist.append(count)



pdf = []

for i in range(256):
    pdf.append(hist[i]/(width*hight))

# print(pdf)

cdf = []

for i in range(256):
    if i==0:
       cdf.append(pdf[i]) 
    cdf.append((pdf[i]+cdf[i-1]))

# print(cdf)

sk = []

for i in range(256):
    sk.append(cdf[i]*255)


hist_equalize = []

for i in range(256):
    hist_equalize.append(math.ceil(sk[i]))




equalize_img = np.zeros((hight, width), dtype=np.uint8)



for i in range(hight):
    for j in range(width):
        equalize_img[i][j] = hist_equalize[gray_img[i][j]]


plt.subplot(4,2,1)
plt.title('old image')
plt.imshow(gray_img)
plt.subplot(4,2,2)
plt.hist(rgb_img.ravel(),256,[0,255])
plt.subplot(4,2,3)
plt.title('Equalized image')
plt.imshow(equalize_img)
plt.subplot(4,2,4)
plt.hist(equalize_img,256,[0,255])

plt.savefig("my_love.jpg")
plt.show()




