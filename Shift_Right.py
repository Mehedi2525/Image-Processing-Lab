import matplotlib.pyplot as plt
import cv2


def main():

    img_path='image2.jpg'
    img=plt.imread(img_path)

    
    gray_convertion=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    row,col=gray_convertion.shape
    
    plt.subplot(4,2,1)
    plt.title("Grayscale")
    plt.imshow(gray_convertion,cmap='gray')
    
    plt.subplot(4,2,2)
    plt.title("Grayscale Histrogram")
    plt.hist(gray_convertion.ravel(),255,[0,255])
    
    move_left_shifted=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    for i in range(0,row):

        for j in range(0,col):

            move_left_shifted[i][j] = gray_convertion[i][j] - 25

            if move_left_shifted[i][j]<0:

                move_left_shifted[i][j]=0
           
    plt.subplot(4,2,3)
    plt.title("Moved Left Image")
    plt.imshow(move_left_shifted,cmap='gray')
    
    plt.subplot(4,2,4)
    plt.title("Moved Left Histrogram")
    plt.hist(move_left_shifted.ravel(),255,[0,255])
    
    move_right_shifted=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    for i in range(0,row):

        for j in range(0,col):

            move_right_shifted[i][j] = gray_convertion[i][j] + 25

            if move_right_shifted[i][j]>255:

                move_right_shifted[i][j]=255

    plt.subplot(4,2,5)
    plt.title("Moved Right Image")
    plt.imshow(move_right_shifted,cmap='gray')
    
    plt.subplot(4,2,6)
    plt.title("Moved Right Histrogram")
    plt.hist(move_right_shifted.ravel(),255,[0,255])
    
    rang_specify_change=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
    for i in range(0,row):

        for j in range(0,col):

            rang_specify_change[i][j] =(gray_convertion[i][j] + 235)/3

            if rang_specify_change[i][j]>225:

                rang_specify_change[i][j]=155

            if rang_specify_change[i][j]<95:

                rang_specify_change[i][j]=130
                
    plt.subplot(4,2,7)
    plt.title("Specific_Range")
    plt.imshow(rang_specify_change,cmap='gray')
    
    plt.subplot(4,2,8)
    plt.title("Specific_Range Histrogram")
    plt.hist(rang_specify_change.ravel(),255,[0,255])
    
    plt.savefig("Output_image.jpg")

    plt.show()
    
if __name__=='__main__':
    main()