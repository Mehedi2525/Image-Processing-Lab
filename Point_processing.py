import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    
    path="./image2.jpg"
    img=plt.imread(path)
    
    grayscale=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
    height,width=grayscale.shape
    
    s1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
    t1=50
    t2=60
    
    for i in range(height):
        for j in range(width):
            
            if(grayscale[i][j]>=t1 and grayscale[i][j]<=t2):
                s1[i][j]=100
                
            else:
                s1[i][j]=10
    
    plt.subplot(4,2,1)
    plt.title("first condition")
    plt.imshow(s1)
    
    s1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
    t1=50
    t2=60
    
    for i in range(height):
        for j in range(width):
            
            if(grayscale[i][j]>=t1 and grayscale[i][j]<=t2):
                s1[i][j]=100

            else:
                s1[i][j]=grayscale[i][j]  
         
    
    plt.subplot(4,2,2)
    plt.title("second condition")
    plt.imshow(s1)
    
    s1=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    c=5

    for i in range(height):
        for j in range(width):
            
          
            s1[i][j]=c*np.log(1+grayscale[i][j])
                
         
    
    plt.subplot(4,2,3)
    plt.title("third condition")
    plt.imshow(s1)
    
    c=5
    epsilon=0.00001
    p=2
    
    for i in range(height):
        for j in range(width):
            
          
            s1[i][j]=pow(c*( grayscale[i][j] + epsilon ),p)
                
         
    
    plt.subplot(4,2,4)
    plt.title("fourth condition")
    plt.imshow(s1)
    
    plt.show()

if __name__ == "__main__":
    main()