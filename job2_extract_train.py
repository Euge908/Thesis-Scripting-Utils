import os
import subprocess as sp


## Making Train Dir
os.makedirs("/mnt/f/Downloads/train_data_merged_full_res/real", exist_ok=True)
os.makedirs("/mnt/f/Downloads/train_data_merged_full_res/attack", exist_ok=True)

###########################################################################################
# Extract Train Sets


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++ OULU Train Files ++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")


print("Cropping OULU Train Files (train and attack)")


# For the train dir: OULU
input_root_dir = "/mnt/f/Downloads/Oulu_NPU/Train_files"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".avi"):
   
        input_dir = input_root_dir + "/" + file
        phone, session, user, file = file.rstrip(".avi").split('_')
        if int(file) == 1:
            output_dir = "/mnt/f/Downloads/train_data_merged_full_res/real"
        else:
            output_dir = "/mnt/f/Downloads/train_data_merged_full_res/attack"

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        


print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM OULU NPU")
print("+++++++++++++++++++++++++++++++++++++++++++++++")




print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++ Replay Attack  Train Files ++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")


print("Cropping Replay Attack Train Files (attack)")

# For train set replay - attack
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/train/attack"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = "/mnt/f/Downloads/train_data_merged_full_res/attack"
        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        

# For train set replay - real
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/train/real"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = "/mnt/f/Downloads/train_data_merged_full_res/real"
        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        


print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM REPLAY ATTACK")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
