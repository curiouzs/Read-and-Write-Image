# READ AND WRITE AN IMAGE
## AIM
To write a python program using OpenCV to do the following image manipulations.
i) Read, display, and write an image.
ii) Access the rows and columns in an image.
iii) Cut and paste a small portion of the image.

## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Choose an image and save it as a filename.jpg
### Step2:
Use imread(filename, flags) to read the file.
### Step3:
Use imshow(window_name, image) to display the image.
### Step4:
Use imwrite(filename, image) to write the image.
### Step5:
End the program and close the output image windows.
## Program:
```python
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








```
## Output:

### i) Read and display the image
![lo](https://user-images.githubusercontent.com/75234646/160963899-b018b18c-a703-45df-8c54-54c5d92b5603.png)

### ii)Write the image

![ws](https://user-images.githubusercontent.com/75234646/160963802-823ae2db-c72a-4ee3-9c39-a3bba4185f0b.png)

### iii)Shape of the Image

![ws](https://user-images.githubusercontent.com/75234646/160963825-3b3b1954-8992-43d1-93b1-5098efc24282.png)

### iv)Access rows and columns



![ar](https://user-images.githubusercontent.com/75234646/160964015-4bb95a46-656a-4095-b3fa-54429582d673.png)

### v)Cut and paste portion of image



![cp](https://user-images.githubusercontent.com/75234646/160964055-55ce357a-5c93-4e48-bd18-aea11ec0b87a.png)

## Result:
Thus the images are read, displayed, and written successfully using the python program.


