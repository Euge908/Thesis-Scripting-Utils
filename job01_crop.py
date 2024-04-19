import os
import subprocess as sp


#balancing datasets
#https://datascience.stackexchange.com/questions/13490/how-to-set-class-weights-for-imbalanced-classes-in-keras
#

#train and validation sets
input_dirs = ["/mnt/f/Downloads/Oulu_NPU/Train_files", 
              "/mnt/f/Downloads/Oulu_NPU/Dev_files", 
              "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/train", 
              "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/devel"
             ]

train_real_output_dir = "/mnt/f/Downloads/train_data_merged_3_frames/real"
train_attack_output_dir = "/mnt/f/Downloads/train_data_merged_3_frames/attack"

dev_real_output_dir = "/mnt/f/Downloads/dev_data_merged_3_frames/real"
dev_attack_output_dir = "/mnt/f/Downloads/dev_data_merged_3_frames/attack"


#make output dirs
print(f"Making the following dirs: {train_real_output_dir}\n, {train_attack_output_dir}\n, {dev_real_output_dir}\n, {dev_attack_output_dir}\n")
os.makedirs(train_real_output_dir, exist_ok=True)
os.makedirs(train_attack_output_dir, exist_ok=True)
os.makedirs(dev_real_output_dir, exist_ok=True)
os.makedirs(dev_attack_output_dir, exist_ok=True)




# For the train dir: OULU
input_root_dir = "/mnt/f/Downloads/Oulu_NPU/Train_files"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".avi"):
   
        input_dir = input_root_dir + "/" + file
        phone, session, user, file = file.rstrip(".avi").split('_')
        # print("File: ", file)
        # print(phone, "|", session, "|", user, "|", file)
        if int(file) == 1:
            output_dir = train_real_output_dir
        else:
            output_dir = train_attack_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        


# For the dev dir: OULU
input_root_dir = "/mnt/f/Downloads/Oulu_NPU/Dev_files"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".avi"):
        input_dir = input_root_dir + "/" + file
        phone, session, user, file = file.rstrip(".avi").split('_')
        
        if int(file) == 1:
            output_dir = dev_real_output_dir
        else:
            output_dir = dev_attack_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        


#For the train dir: Replay

## Attack
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/train/attack"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = train_attack_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        
        

## Real
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/train/real"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = train_real_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        
        
#For the dev dir: Replay

## Attack
print("\n========================================================")
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/devel/attack"
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = dev_attack_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        
        

## Real
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/devel/real"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = dev_real_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        


        
# test_input = "/home/eugene/Thesis Helper Functions/test_input/attack/attack_client016_session01_print_fixed_mobile_photo_lightoff.mov"
# test_output = "/home/eugene/Thesis Helper Functions/test_output"


# sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", test_input, "--dest", test_output])