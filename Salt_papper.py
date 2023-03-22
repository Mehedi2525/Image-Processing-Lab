import matplotlib.pyplot as plt
import cv2
import numpy as np
import random

def main():


    def salt_papper(img):
        
        for i in range(random.randint(0,80000)):
            
            x_cor=random.randint(0,height-1)
            y_cor=random.randint(0,width-1)
        
            img[x_cor][y_cor]=255
        
        for i in range(random.randint(0,80000)):
            
            x_cor=random.randint(0,height-1)
            y_cor=random.randint(0,width-1)
        
            img[x_cor][y_cor]=0
            
        
        return img
        
    
    
    
    path="./image4.png"
    img=cv2.imread(path,0)
    
    height,width=img.shape
    
    noice_img=salt_papper(img)
    
    gaussian=cv2.GaussianBlur(noice_img,(3,3),cv2.BORDER_DEFAULT)
    
    median=cv2.medianBlur(noice_img,3)

    plt.subplot(4,2,1)
    plt.title("noice image")
    plt.imshow(noice_img)
    
    plt.subplot(4,2,2)
    plt.title("gaussian")
    plt.imshow(gaussian)
    
    plt.subplot(4,2,3)
    plt.title("median")
    plt.imshow(median)
    
    
    avg=np.ones((3,3),np.int8)/9
    proces=cv2.filter2D(noice_img,-1,avg)
    
    plt.subplot(4,2,4)
    plt.title("average")
    plt.imshow(proces)
    
    
    plt.show()


if __name__ == "__main__":
	main()