import os
import subprocess as sp


#balancing datasets
#https://datascience.stackexchange.com/questions/13490/how-to-set-class-weights-for-imbalanced-classes-in-keras


test_real_output_dir = "/mnt/f/Downloads/test_data_merged_3_frames/real"
test_attack_output_dir = "/mnt/f/Downloads/test_data_merged_3_frames/attack"

print(f"Making the following dirs: {test_real_output_dir}\n, {test_attack_output_dir}\n")
os.makedirs(test_real_output_dir, exist_ok=True)
os.makedirs(test_attack_output_dir, exist_ok=True)


# For the test dir: OULU
input_root_dir = "/mnt/f/Downloads/Oulu_NPU/Test_files"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".avi"):
   
        input_dir = input_root_dir + "/" + file
        phone, session, user, file = file.rstrip(".avi").split('_')
        # print("File: ", file)
        # print(phone, "|", session, "|", user, "|", file)
        if int(file) == 1:
            output_dir = test_real_output_dir
        else:
            output_dir = test_attack_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        

#For the test dir: Replay
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/train/attack"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = train_attack_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        
        
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM OULU NPU")
print("+++++++++++++++++++++++++++++++++++++++++++++++")


## Real
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/test/real"
print("\n========================================================")
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = test_real_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        
        
## Attack
print("\n========================================================")
input_root_dir = "/mnt/f/Downloads/Replay-Attack/replay-mobile/database/test/attack"
print(f"Extracting Faces from {input_root_dir}")
for file in os.listdir(input_root_dir):
    if file.endswith(".mov"):
        input_dir = input_root_dir + "/" + file        
        output_dir = test_attack_output_dir

        sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        

print("+++++++++++++++++++++++++++++++++++++++++++++++")
print("FINISHED EXTRACTING FACES FROM REPLAY ATTACK")
print("+++++++++++++++++++++++++++++++++++++++++++++++")

        
# test_input = "/home/eugene/Thesis Helper Functions/test_input/attack/attack_client016_session01_print_fixed_mobile_photo_lightoff.mov"
# test_output = "/home/eugene/Thesis Helper Functions/test_output"


# sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", test_input, "--dest", test_output])