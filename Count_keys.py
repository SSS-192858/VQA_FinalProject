import json

# Assuming your JSON file is named data.json
with open('output_questions_answers.json', 'r') as f:
    data = json.load(f)

# Extracting keys from the JSON data
keys = list(data.keys())

with open('output_image_questions.json', 'r') as f1:
    data1 = json.load(f1)

unique_keys = set()
for key, value_list in data1.items():
    for item in value_list:
        # print(item)
        if str(item['question_id']) in keys:
            unique_keys.add(key)
# Counting the number of unique image IDs
unique_image_ids_count = len(unique_keys)

print("Number of unique image IDs:", unique_image_ids_count)