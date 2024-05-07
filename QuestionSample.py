import os
import json

# Function to read the question dataset from a JSON file
def read_question_dataset(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

# Function to extract image ID from filename
def extract_image_id(filename):
    # Assuming the filename format is "COCO_XXXXXX.jpg" where XXXXXX is the image ID
    return int(filename.split('_')[-1].split('.')[0].lstrip('0'))

# Read the question dataset from the JSON file
question_dataset_path = "./drive_download/v2_OpenEnded_mscoco_train2014_questions.json"
questions = read_question_dataset(question_dataset_path)
# print(questions.keys())

questions_final = questions['questions']


print(questions_final[0])
# Dictionary to store questions for each image ID
image_questions = {}

# Iterate through the folder containing images
images_folder = "./Images_train/Subset_train2014/"
for filename in os.listdir(images_folder):
    if filename.endswith(".jpg"):
        image_id = extract_image_id(filename)
        # Check if image ID exists in the question dataset
        # print(image_id)
        if any(question['image_id'] == image_id for question in questions_final):
            # Get questions for the image ID
            image_questions[image_id] = [question for question in questions_final if question['image_id'] == image_id]


# Now image_questions contains the questions grouped by image ID
# You can access questions for a specific image ID like this:
output_json_file = "./output_image_questions.json"
with open(output_json_file, 'w') as file:
    json.dump(image_questions, file, indent=4)

print("Output JSON file written successfully:", output_json_file)
