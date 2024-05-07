import os

def count_files(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Error: Directory does not exist")
        return
    
    # Get list of files in the directory
    files = os.listdir(directory)
    
    # Count the number of files
    num_files = len(files)
    
    return num_files

# Example usage
directory_path = "./Images_train/train2014/"
num_files = count_files(directory_path)
print("Number of files in directory:", num_files)