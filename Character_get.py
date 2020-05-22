import cv2
import numpy as np
import os

image = cv2.imread('Images/prescription_1_crop.jpg')

# convert into grey
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thresh = cv2.threshold(grey_image,85,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Thresh Image', thresh)

# kernel = np.ones((3,3), np.uint8) # adjust the size of the rectangle

# image_dilation = cv2.dilate(thresh, kernel, iterations=1) # iterations can be used to adjust the size of the word cover

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# contours, hierarchy = cv2.findContours(image_dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("Number of contours is :"+str(len(contours)))

path = "C:/Users/DELL/Desktop/Handwriting ROI detetction/Output"

i=0
for cnt in contours:
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
	#following if statement is to ignore the noises and save the images which are of normal size(character)
	#In order to write more general code, than specifying the dimensions as 100,
	# number of characters should be divided by word dimension
	#save individual images
	ROI = thresh[y:y+h,x:x+w]
	print(str(i) + "image" + str(w) + "and" + str(h))
	cv2.imwrite(os.path.join(path,str(i)+".jpg"), ROI)
	i=i+1
	# if w>100 and h>100:
	# 	#save individual images
	# 	ROI = thresh[y:y+h,x:x+w]
	# 	cv2.imwrite(os.path.join(path,str(i)+".jpg"), ROI)
	# 	i=i+1

cv2.namedWindow('BindingBox', cv2.WINDOW_NORMAL)
cv2.imshow('BindingBox',image)

cv2.waitKey(0)
cv2.destroyAllWindows()