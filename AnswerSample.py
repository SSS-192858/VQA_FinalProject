import os
import json

# Function to read the question dataset from a JSON file
def read_question_dataset(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        answers = json.load(file)
    return answers

# Function to extract image ID from filename
def extract_image_id(filename):
    # Assuming the filename format is "COCO_XXXXXX.jpg" where XXXXXX is the image ID
    return int(filename.split('_')[-1].split('.')[0].lstrip('0'))

# Read the question dataset from the JSON file
answers_dataset_path = "./v2_mscoco_train2014_annotations.json"
answers = read_question_dataset(answers_dataset_path)
# print(questions.keys())

ans_final = answers['annotations']

print("Done")
print(ans_final[0])



# import json

# Function to read the question dataset from a JSON file
def read_question_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to create a dictionary of question IDs and corresponding answers
def create_questions_answers_dict(data, ans_final):
    questions_answers_dict = {}

    for question_number, questions in data.items():
        for question in questions:
            question_id = question['question_id']
            # Search for the question ID in the ans_final list
            for ans in ans_final:
                if ans['question_id'] == question_id:
                    print(question_number)
                    questions_answers_dict[int(question_id)] = ans['answers']
                    break
        # break
    return questions_answers_dict

def write_json_file(output_file, data):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

# Read the data from the JSON file
file_path = "./output_image_questions.json"  # Update with the actual file path
data = read_question_data(file_path)

# Match question IDs with corresponding answers
questions_answers_dict = create_questions_answers_dict(data, ans_final)

# Print the dictionary containing question numbers and their corresponding answers
output_file = "output_questions_answers.json"

# Write the questions and answers dictionary to a JSON file
write_json_file(output_file, questions_answers_dict)

print("JSON file containing questions and answers written successfully:", output_file)
# # Dictionary to store questions for each image ID
# image_ans = {}

# # Iterate through the folder containing images
# images_folder = "./Images_train/Subset_train2014/"
# for filename in os.listdir(images_folder):
#     if filename.endswith(".jpg"):
#         image_id = extract_image_id(filename)
#         # Check if image ID exists in the question dataset
#         # print(image_id)
#         if any(answer['image_id'] == image_id for answer in ans_final):
#             # Get questions for the image ID
#             image_ans[image_id] = [answer for answer in ans_final if answer['image_id'] == image_id]


# # Now image_questions contains the questions grouped by image ID
# # You can access questions for a specific image ID like this:
# output_json_file = "./output_image_questions.json"
# with open(output_json_file, 'w') as file:
#     json.dump(image_questions, file, indent=4)

# print("Output JSON file written successfully:", output_json_file)


# def extract_question_ids(json_file):
#     with open(json_file, 'r') as file:
#         data = json.load(file)
    
#     question_ids = []
#     for image_id, questions in data.items():
#         for question in questions:
#             question_ids.append(question['question_id'])
    
#     return question_ids
