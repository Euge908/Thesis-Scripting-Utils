import os
from PIL import Image

def resize_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)
    
    # Iterate through each file in the input folder
    for file in files:
        # Construct the full path of the input file
        input_path = os.path.join(input_folder, file)
        
        # Check if the file is a valid image file
        if os.path.isfile(input_path) and file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            # Open the image
            with Image.open(input_path) as img:
                # Get the new dimensions (80% of original size)
                width, height = img.size
                new_width = int(width * 0.8)
                new_height = int(height * 0.8)
                
                # Resize the image
                resized_img = img.resize((new_width, new_height))
                
                # Construct the full path of the output file
                output_path = os.path.join(output_folder, file)
                
                # Save the resized image to the output folder
                resized_img.save(output_path)
                print(f"Resized {file} and saved to {output_path}")



## Resize test images
resize_images(input_folder = "/mnt/f/Downloads/test_data_merged_full_res/spoofing", output_folder="/mnt/f/Downloads/test_data_merged_resized_80/spoofing")
resize_images(input_folder = "/mnt/f/Downloads/test_data_merged_full_res/living", output_folder="/mnt/f/Downloads/test_data_merged_resized_80/living")


## Resize train images
resize_images(input_folder = "/mnt/f/Downloads/train_data_merged_full_res/spoofing", output_folder="/mnt/f/Downloads/train_data_merged_resized_80/spoofing")
resize_images(input_folder = "/mnt/f/Downloads/train_data_merged_full_res/living", output_folder="/mnt/f/Downloads/train_data_merged_resized_80/living")
