import os
import shutil

def copy_every_third_file(source_dir, dest_dir):
    try:
        # Ensure destination directory exists
        os.makedirs(dest_dir, exist_ok=True)

        # Get a list of files in the source directory
        files = os.listdir(source_dir)

        # Filter out only files (not directories)
        files = [file for file in files if os.path.isfile(os.path.join(source_dir, file))]

        # Select every third file
        selected_files = files[2::3]

        # Copy selected files to the destination directory
        for file in selected_files:
            source_path = os.path.join(source_dir, file)
            dest_path = os.path.join(dest_dir, file)
            shutil.copy2(source_path, dest_path)
            print(f"Copied: {file} -> {dest_path}")

        print("Copy operation completed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
source_directory = "/mnt/f/Downloads/train_data_merged/real"
destination_directory = "/mnt/f/Downloads/train_data_merged_3_frames/real"

copy_every_third_file(source_directory, destination_directory)