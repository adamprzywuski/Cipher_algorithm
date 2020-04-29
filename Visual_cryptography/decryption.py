import cv2
import random
import numpy as np

#first way
def decrypting(path1,path2):

    img1=cv2.imread(path1,0)
    img2=cv2.imread(path2,0)
    pic=np.zeros(shape=[100, 100], dtype=np.uint8)
    pic_assist=[0,0,0,0]

    x,y=pic.shape

    for a in range(x):
        for b in range(y):
            pic_assist[0]=img1[a*2][b*2]+img2[a*2][b*2]
            pic_assist[1]=img1[a*2+1][b*2]+img2[a*2+1][b*2]
            pic_assist[2] = img1[a * 2][b * 2+1] + img2[a * 2][b * 2+1]
            pic_assist[3] = img1[a * 2+1][b * 2+1] + img2[a * 2+1][b * 2+1]

            for k in pic_assist:
                if(k!=254):
                    pic[a][b] = 254
                    break
                else:
                    pic[a][b]=0

    cv2.imwrite("visual_.png",pic)

    print("done")
#better way
def decryt(path1,path2):
    img1=cv2.imread(path1,0)
    img2=cv2.imread(path2,0)
    pic=np.zeros(shape=[200, 200], dtype=np.uint8)

    x,y=pic.shape

    for a in range(x):
        for b in range(y):
            pic[a][b]=(img1[a][b]+img2[a][b])/2

    cv2.imwrite("visual.png", pic)


if __name__ == '__main__':
    decrypting("one.png","two.png")
    decryt("one.png","two.png")