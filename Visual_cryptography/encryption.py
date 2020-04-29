import cv2
import random
import numpy as np


#2 udzialy 100x100 obrazek



def encrypt(file):
    #creating and opening images
    img=cv2.imread(file,0)
    pic1=np.zeros(shape=[200, 200, 1])

    pic2=np.zeros(shape=[200, 200], dtype=np.uint8)

    x,y=img.shape
    for a in range(x):
        for b in range(y):
            if(img[a][b]<255 and img[a][b]>0):
                img[a][b]=254

    for a in range(x):
        for b in range(y):
            rand=random.randint(0,1)
            main_pixel=img[a][b]

            #black pixel
            if(main_pixel==0):
                if(rand==0):
                    pic1[int(a*2)][b*2]=254
                    pic1[a*2+1][b*2]=254
                    pic1[a*2][b*2+1]=0
                    pic1[a*2+1,b*2+1]=0

                    pic2[int(a*2)][int(b*2)]=0
                    pic2[a*2+1][b*2]=0
                    pic2[a*2][b*2+1]=254
                    pic2[a*2+1][b*2+1]=254

                elif(rand==1):

                    pic1[int(a*2)][int(b*2)]=0
                    pic1[a*2+1][b*2]=0
                    pic1[a*2][b*2+1]=254
                    pic1[a*2+1][b*2+1]=254

                    pic2[int(a*2)][int(b*2)]=254
                    pic2[a*2+1][b*2]=254
                    pic2[a*2][b*2+1]=0
                    pic2[a*2+1][b*2+1]=0


            #while pixel
            elif(main_pixel==254):
                #dosomething
                if(rand==0):
                    pic1[int(a*2),int(b*2)]=254
                    pic1[a*2+1][b*2]=254
                    pic1[a*2][b*2+1]=0
                    pic1[a*2+1][b*2+1]=0

                    pic2[int(a*2)][int(b*2)]=254
                    pic2[a*2+1][b*2]=254
                    pic2[a*2][b*2+1]=0
                    pic2[a*2+1][b*2+1]=0

                else:
                    pic2[int(a*2)][int(b*2)]=0
                    pic2[a*2+1][b*2]=0
                    pic2[a*2][b*2+1]=254
                    pic2[a*2+1][b*2+1]=254

                    pic1[int(a*2)][int(b*2)]=0
                    pic1[a*2+1][b*2]=0
                    pic1[a*2][b*2+1]=254
                    pic1[a*2+1][b*2+1]=254


    cv2.imwrite("one.png",pic1)
    cv2.imwrite("two.png",pic2)

if __name__ == '__main__':
    encrypt("visual_crypt.png")
