# 2. Load the VQA dataset
from datasets import load_dataset
import random
from pathlib import Path
import os
import shutil

# Load the dataset
vqa = load_dataset("VQAv2.py", data_dir="VQAv2_Dataset")

# 3. Random Sampling (take 1/4th of a random subset of questions)
# Let's say you want to sample from the training dataset
train_data = vqa["train"]

# Shuffle the dataset and take a random subset
random_subset = train_data.shuffle(seed=42).select(range(len(train_data) // 4))

# 4. Download Corresponding Images
# Find the image URLs for the selected questions
image_dir = Path("downloaded_images")
image_dir.mkdir(parents=True, exist_ok=True)

# Download the required images (assuming URLs to images are given)
# Note: This step will vary depending on how the images are referenced/stored.
image_ids = [item["image_id"] for item in random_subset]
base_image_url = "http://images.cocodataset.org/zips/"  # Placeholder, adjust to actual source

for image_id in set(image_ids):
    # Construct the image file name
    image_filename = f"COCO_train2014_{str(image_id).zfill(12)}.jpg"
    image_url = f"{base_image_url}/{image_filename}"

    # Download the image and save it to the local directory
    image_path = image_dir / image_filename

    # Download the image (using a library like requests or urllib)
    # Sample code using urllib.request
    import urllib.request

    try:
        urllib.request.urlretrieve(image_url, str(image_path))
    except Exception as e:
        print(f"Error downloading image {image_id}: {e}")

# 5. Prepare Output
# Create a new dataset containing the random subset and the corresponding images
# You can save this data to disk or process it further as needed
# This could be exporting as a CSV/JSON, or using another data structure.

import json

# Example: Save the question data and the image paths to a JSON file
output_data = {
    "questions": [{"question": item["question"], "question_id": item["question_id"], "image_path": str(image_dir / f"COCO_train2014_{str(item['image_id']).zfill(12)}.jpg")} for item in random_subset],
}

# Save to JSON
with open("random_vqa_subset.json", "w") as f:
    json.dump(output_data, f, indent=2)
