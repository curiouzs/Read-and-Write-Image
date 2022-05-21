# Developed By:LOKESH KRISHNA .M
# Register Number:212220230030
# To Read,display the image
import cv2
bw=cv2.imread("and.jpeg",1)
cv2.imshow('lokesh',bw)
cv2.waitKey(0)


# To write the image
cv2.imwrite("pillar.jpeg",bw)


# Find the shape of the Image
print(bw.shape)


# To access rows and columns
import random
for i in range(100):
    for j in range(bw.shape[1]):
        bw[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('accessing row and column',bw)
cv2.waitKey(0)


# To cut and paste portion of image

bw2=cv2.imread("and.jpeg",1)
tag=bw2[890:990,900:1000]
bw2[800:900,1000:1100]=tag
cv2.imshow("cutting portion",bw2)
cv2.waitKey(0)

