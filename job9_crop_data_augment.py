import os
import subprocess as sp
from PIL import Image
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

import cv2
import argparse
from deepface import DeepFace
import matplotlib.pyplot as plt
from retinaface import RetinaFace
from mtcnn import MTCNN



def retina_crop(input_path, output_path):
    faces = RetinaFace.extract_faces(input_path, align=False)
    face = cv2.cvtColor(faces[0], cv2.COLOR_BGR2RGB) # convert from bgr to rgb
    print(f"Cropping {input_path}")
    cv2.imwrite(output_path, face)



# def mtcnn_crop(input_image_path, output_path):
def mtcnn_crop(image_path, output_path):
    detector = MTCNN() 
    img=cv2.imread(image_path)
    data=detector.detect_faces(img)
    biggest=0
    if data !=[]:
        for faces in data:
            box=faces['box']            
            # calculate the area in the image
            area = box[3]  * box[2]
            if area>biggest:
                biggest=area
                bbox=box 
        bbox[0]= 0 if bbox[0]<0 else bbox[0]
        bbox[1]= 0 if bbox[1]<0 else bbox[1]
        img=img[bbox[1]: bbox[1]+bbox[3],bbox[0]: bbox[0]+ bbox[2]] 
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert from bgr to rgb

        print("\n--------------------")
        print(f"image_path is {output_path}")
        print("\n--------------------")
        
        cv2.imwrite(output_path, img)
        return True
    else:
        return False



# test_real_output_dir = "/mnt/f/Downloads/Data Augment Commons/real"
# test_attack_output_dir = "/mnt/f/Downloads/Data Augment Commons/attack"

# print(f"Making the following dirs: {test_real_output_dir}\n, {test_attack_output_dir}\n")
# os.makedirs(test_real_output_dir, exist_ok=True)
# os.makedirs(test_attack_output_dir, exist_ok=True)


# ## Real
# input_root_dir = "/mnt/f/Downloads/Data Augment Commons/real"
# print("\n========================================================")
# print(f"Extracting Faces from {input_root_dir}")

# off_files = []
# for file in os.listdir(input_root_dir):
#     if file.endswith(".jpg"):
#         input_dir = input_root_dir + "/" + file        
#         out_file_dir_name = test_real_output_dir + '/' + file
#         print(f"Extracting Faces from and to {input_dir} to {out_file_dir_name}")
#         res = mtcnn_crop(input_dir, out_file_dir_name)
#         if res == False:
#             off_files.append(input_dir)

#         # retina_crop(input_dir, out_file_dir_name)


# print("OFF FILES")
# print(off_files)

# ## Attack
# input_root_dir = "/mnt/f/Downloads/Data Augment Commons/attack"
# print("\n========================================================")
# print(f"Extracting Faces from {input_root_dir}")

# off_files = []
# for file in os.listdir(input_root_dir):
#     if file.endswith(".jpg"):
#         input_dir = input_root_dir + "/" + file        
#         out_file_dir_name = test_attack_output_dir + '/' + file
#         print(f"Extracting Faces from and to {input_dir} to {out_file_dir_name}")
#         res = mtcnn_crop(input_dir, out_file_dir_name)
#         if res == False:
#             off_files.append(input_dir)
#         # retina_crop(input_dir, out_file_dir_name)



# print("OFF FILES")
# print(off_files)





## Temp Faces
input_root_dir = "/mnt/f/Downloads/thesis-test-faces/temp-faces"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")

off_files = []
for file in os.listdir(input_root_dir):
    if file.endswith(".jpg"):
        input_dir = input_root_dir + "/" + file        
        out_file_dir_name = input_root_dir + '/' + file
        print(f"Extracting Faces from and to {input_dir} to {out_file_dir_name}")
        res = mtcnn_crop(input_dir, out_file_dir_name)
        if res == False:
            off_files.append(input_dir)

        # retina_crop(input_dir, out_file_dir_name)


