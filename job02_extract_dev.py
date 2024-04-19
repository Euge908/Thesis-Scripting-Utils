import os
import subprocess as sp


#balancing datasets
#https://datascience.stackexchange.com/questions/13490/how-to-set-class-weights-for-imbalanced-classes-in-keras

## Making Dev Dir

os.makedirs("/mnt/f/Downloads/dev_data_merged_full_res/real", exist_ok=True)
os.makedirs("/mnt/f/Downloads/dev_data_merged_full_res/attack", exist_ok=True)


###########################################################################################
# Extract Evaluation Sets

# Extract Dev Sets


print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++ OULU  Dev Files ++++++++++++++++++++++++++++++++ ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")


print("Cropping OULU Dev Files (train and attack)")


# For the dev dir: OULU
input_root_dir = "/mnt/f/Downloads/Oulu_NPU/Dev_files"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".avi"):
   
        input_dir = input_root_dir + "/" + file
        phone, session, user, file = file.rstrip(".avi").split('_')
        if int(file) == 1:
            output_dir = "/mnt/f/Downloads/dev_data_merged_full_res/real"
        else:
            output_dir = "/mnt/f/Downloads/dev_data_merged_full_res/attack"

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        


print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM OULU NPU")
print("+++++++++++++++++++++++++++++++++++++++++++++++")




print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++ Replay Attack  Dev Files ++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")


print("Cropping Replay Attack Dev Files (attack)")

# For dev set replay - attack
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/devel/attack"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = "/mnt/f/Downloads/dev_data_merged_full_res/attack"
        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        

# For dev set replay - real
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/devel/real"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = "/mnt/f/Downloads/dev_data_merged_full_res/real"
        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        


print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM REPLAY ATTACK")
print("+++++++++++++++++++++++++++++++++++++++++++++++")






