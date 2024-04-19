import cv2
import os
import shutil

def resize_image(input_path, output_path, max_width=720):
    print(f"Resizing {input_path} with max_width of {max_width} to {output_path}")
    # Read the image
    image = cv2.imread(input_path)

    # Get the original width and height
    original_height, original_width = image.shape[:2]

    # Resize only if the width exceeds the specified maximum
    if original_width > max_width:
        # Calculate the aspect ratio
        aspect_ratio = original_width / original_height

        # Calculate the new height based on the maximum width
        new_width = max_width
        new_height = int(new_width / aspect_ratio)

        # Resize the image
        resized_image = cv2.resize(image, (new_width, new_height))

        # Save the resized image
        cv2.imwrite(output_path, resized_image)
    else:
        # If the image doesn't need resizing, just copy it to the output path
        shutil.copyfile(input_path, output_path)

if __name__ == "__main__":

    # Input and output directories
    input_directory = "/mnt/f/Downloads/thesis-train-faces-raw/real/"
    output_directory = "/mnt/f/Downloads/thesis-train-faces/living/"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each image in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", "JPG")):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            # Resize the image if necessary
            resize_image(input_path, output_path)

    # Input and output directories
    input_directory = "/mnt/f/Downloads/photopaper"
    output_directory = "/mnt/f/Downloads/photopaper-resized"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each image in the input directory
    for filename in os.listdir(input_directory):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", "JPG")):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)

            # Resize the image if necessary
            resize_image(input_path, output_path)


    
    
    
    print("Image resizing completed.")