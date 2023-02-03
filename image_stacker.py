import cv2
import numpy as np
import os

# input the folder name with images to stack
# folder must me in the same directory as the script
# images shoould be same in size

np.seterr(over ="ignore") # hide numpy errors

# image folder 
folder = input("Enter folder name: ") + "/"

# list all the images in folder
img_lst = [folder + i for i in os.listdir(folder)] 

# get number of row and columns in an image
img = cv2.imread(img_lst[0] , -1) 
print("processing image 1 (" + img_lst[0], ", rows: " + str(img.shape[0]) + ", columns: " + str(img.shape[1]) + ")")

rows = img.shape[0]
columns = img.shape[1]

# output image
final_img = np.asarray(img)
final_img.setflags(write=True)

# stacking
img_num = 1; row = 0; column = 0; color = 0

while img_num< len(img_lst): # read all the images int he list

    img = np.asarray(cv2.imread(img_lst[img_num] , -1))
    print("processing image " + str(img_num + 1))
    
    # read all the pixels 
    while row< rows:
        while column< columns:
            while color<3:
                # average the color of image
                final_img[row][column][color] = (int(final_img[row][column][color]) + int(img[row][column][color]))/2
                color += 1
            
            color =0
            column += 1
        
        column = 0
        row += 1

    row = 0
    img_num += 1

print("finished")              
cv2.imwrite(folder + "final.jpg", final_img) # write the final image