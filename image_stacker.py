import cv2
import numpy as np
import os

# input the folder name with images to stack
# folder must me in the same directory as the script
# images shoould be same in size

np.seterr(over ="ignore") # hide numpy errors

# image folder 
#folder = input("Enter folder name: ") + "/"
folder = "sample/"

# list all the images in folder
img_lst = [folder + i for i in os.listdir(folder)] 

# get number of row and columns in an image
img = cv2.imread(img_lst[0] , -1) 
print("processing image 1 (" + img_lst[0] + ", rows: " + str(img.shape[0]) + ", columns: " + str(img.shape[1]) + ")")

# output image
final_img = np.asarray(img)
final_img.setflags(write=True)

#stacking
img_num = 1

while img_num< len(img_lst):

    img = np.asarray(cv2.imread(img_lst[img_num] , -1))
    print("processing image " + str(img_num + 1) + " (" + img_lst[img_num] + ", rows: " + str(img.shape[0]) + ", columns: " + str(img.shape[1]) + ")")
    final_img = ((final_img.astype(np.int16) + img.astype(np.int16))//2).astype(np.uint8)
    img_num += 1

print("finished")              
cv2.imwrite(folder + "final.jpg", final_img) # write the final image