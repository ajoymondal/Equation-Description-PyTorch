import cv2
import numpy as np
from PIL import ImageFilter, Image
import os
import os.path
import sys
import math

extra_part = 40
half_part = 20

image_path = '../3_generate_pdf_to_image/3_inequality_pdf_to_image/'
crop_image_path = '3_inequality_crop_image/'

if not os.path.exists(crop_image_path):
    os.makedirs(crop_image_path)

for filename in os.listdir(image_path):
    if filename.endswith('.png'): 
        print(filename)
        #read each images from folder
        img = cv2.imread(os.path.join(image_path,filename)) 
        height, width, chal = img.shape
        for i in range(400):
            flag =0
            for j in range (width-1):
                if img[i,j,0]==255 and img[i,j+1,0]==0:
                    flag = 1
                    col_index1 =j
                    break
            if flag ==1:
                row_index1 = i
                break
        #print('height, width', row_index1, col_index1)
        
        # find bottom point
        for i in range(400, 100, -1):
            flag =0
            for j in range (width-1):
                if img[i,j,0]==255 and img[i,j+1,0]==0:
                    flag = 1
                    col_index2 =j
                    break
            if flag ==1:
                row_index2 = i
                break
        #print('height, width', row_index2, col_index2)

        #find left point
        for j in range(width-1):
            flag =0
            for i in range (400):
                if img[i,j,0]==255 and img[i+1,j,0]==0:
                    flag = 1
                    row_index3 =i
                    break
            if flag ==1:
                col_index3 = j
                break
        #print('height, width', row_index3, col_index3)

        #find right point
        for j in range(width-1, 0, -1):
            flag =0
            for i in range (400):
                if img[i,j,0]==255 and img[i+1,j,0]==0:
                    flag = 1
                    row_index4 =i
                    break
            if flag ==1:
                col_index4 = j
                break
        #print('height, width', row_index4, col_index4)
        
        #find four corner points of crop equation
        #find (x1, y1)
        if col_index3<col_index1:
            y1 = col_index3
        else:
            y1 = col_index1    

        if row_index3<row_index1:
            x1 = row_index3
        else:
            x1 = row_index1     

        #find(x2,y2)
        if col_index1<col_index4:
            y2 = col_index4
        else:
            y2 = col_index1     
        
        if row_index1<row_index4:
            x2 = row_index1
        else:
            x2 = row_index4

        #fin(x3, y3) 
        if col_index2<col_index4:
            y3 = col_index4
        else:
            y3 = col_index2

        if row_index2<row_index4:
            x3 = row_index4
        else:
            x3 = row_index2

        #find(x4, y4) 
        if col_index3<col_index2:
            y4 =col_index3
        else:
            y4 = col_index2

        if row_index3<row_index2:
            x4 = row_index2
        else:
            x4 = row_index3

        m = 850-y2-1 
        crop_height = abs(x1-x4)+10
        if m>5:
            crop_width = abs(y1-y2)+5
        else:
            crop_width = abs(y1-y2)

        crop_image = np.zeros((crop_height+extra_part, crop_width+extra_part, 3), np.uint8) 

        for i in range (crop_height+extra_part):
            for j in range(crop_width+extra_part):
                if crop_image[i,j,0]==0 and crop_image[i,j,1]==0 and crop_image[i,j,2]==0 :
                    crop_image[i,j,0] =255
                    crop_image[i,j,1] =255
                    crop_image[i,j,2] =255

        for i in range (crop_height):
            for j in range (crop_width):
                crop_image[i+half_part, j+half_part, 0] = img[i+x1, j+y1, 0]
                crop_image[i+half_part, j+half_part, 1] = img[i+x1, j+y1, 1]
                crop_image[i+half_part, j+half_part, 2] = img[i+x1, j+y1, 2]            

        crop_image1 = Image.fromarray(crop_image)
        crop_image1.save(os.path.join(crop_image_path,filename),'PNG')
