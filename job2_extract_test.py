import os
import subprocess as sp


## Making Test Dir
os.makedirs("/mnt/f/Downloads/test_data_merged_full_res/real", exist_ok=True)
os.makedirs("/mnt/f/Downloads/test_data_merged_full_res/attack", exist_ok=True)


###########################################################################################
# Extract Test Sets


print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++ OULU Test Files ++++++++++++++++++++++++++++++++ ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")


print("Cropping OULU Test Files (train and attack)")


# For the test dir: OULU
input_root_dir = "/mnt/f/Downloads/Oulu_NPU/Test_files"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".avi"):
   
        input_dir = input_root_dir + "/" + file
        phone, session, user, file = file.rstrip(".avi").split('_')
        if int(file) == 1:
            output_dir = "/mnt/f/Downloads/test_data_merged_full_res/real"
        else:
            output_dir = "/mnt/f/Downloads/test_data_merged_full_res/attack"

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        


print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM OULU NPU")
print("+++++++++++++++++++++++++++++++++++++++++++++++")




print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++ Replay Attack Test Files ++++++++++++++++++++++++++++++++ ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ")


print("Cropping Replay Attack Test Files (attack)")

# For test set replay - attack
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/test/attack"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = "/mnt/f/Downloads/test_data_merged_full_res/attack"
        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        

# For test set replay - real
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/test/real"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = "/mnt/f/Downloads/test_data_merged_full_res/real"
        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir, "--overwrite", "0"])        



print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM REPLAY ATTACK")
print("+++++++++++++++++++++++++++++++++++++++++++++++")


