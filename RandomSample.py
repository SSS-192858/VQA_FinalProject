import os
import random
import shutil

def sample_and_copy(source_dir, target_dir, num_samples):
    # Check if the source directory exists
    if not os.path.isdir(source_dir):
        print("Error: Source directory does not exist")
        return
    
    # Check if the target directory exists, if not create it
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Get list of files in the source directory
    files = os.listdir(source_dir)
    
    # Randomly sample files
    sampled_files = random.sample(files, num_samples)
    
    # Copy sampled files to target directory
    for file in sampled_files:
        source_file_path = os.path.join(source_dir, file)
        target_file_path = os.path.join(target_dir, file)
        shutil.copy(source_file_path, target_file_path)

# Example usage
source_directory = "./Images_train/train2014"
target_directory = "./Images_train/Subset_train2014"
num_samples = 20700

sample_and_copy(source_directory, target_directory, num_samples)
