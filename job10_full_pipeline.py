import os
import subprocess as sp

felix_dirs = ["/mnt/f/Downloads/Felix_Videos/Felix Vids/Live", "/mnt/f/Downloads/Felix_Videos/Felix Vids/Spoof"]
output_dir = "/mnt/f/Downloads/Extracted_Felix_faces"

## Make Output Dir
os.makedirs(output_dir, exist_ok=True)



## Extract Frames from Video
for files in felix_dirs:
    print(f"=================={files}==================")
    for file in os.listdir(files):
        if (file.endswith("mp4")):
            input_dir = files + "/" + file
            print(file)
            sp.run(["python3", "/home/eugene/Thesis Helper Functions/crop_all_vid_faces.py", "--source", input_dir, "--dest", output_dir])        

