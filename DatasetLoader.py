# Ensure required libraries are installed
# !pip install datasets pandas  # Uncomment this line if you're in a Jupyter notebook

from VQA_FinalProject.VQAv2.VQAv2 import VQAv2Dataset  # Import the custom dataset class
# Import necessary modules
import datasets
import json
import pandas as pd
from pathlib import Path

# Define dataset information (as provided in the original script)
_CITATION = """\
@InProceedings{VQA,
author = {Stanislaw Antol and others},
title = {VQA: Visual Question Answering},
booktitle = {International Conference on Computer Vision (ICCV)},
year = {2015},
} 
"""

_DESCRIPTION = """\
VQA is a new dataset containing open-ended questions about images. These questions require an understanding of vision, language, and commonsense knowledge to answer.
"""

_HOMEPAGE = "https://visualqa.org"

_LICENSE = "CC BY 4.0"

_URLS = {
    "questions": {
        "train": "https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Train_mscoco.zip",
        "val": "https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Val_mscoco.zip",
        "test-dev": "https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Test_mscoco.zip",
        "test": "https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Test_mscoco.zip",
    },
    "annotations": {
        "train": "https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Train_mscoco.zip",
        "val": "https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Val_mscoco.zip",
    },
    "images": {
        "train": "http://images.cocodataset.org/zips/train2014.zip",
        "val": "http://images.cocodataset.org/zips/val2014.zip",
        "test-dev": "http://images.cocodataset.org/zips/test2015.zip",
        "test": "http://images.cocodataset.org/zips/test2015.zip",
    },
}

# Create a download manager and download/extract the data
dl_manager = datasets.DownloadManager()  # Set up a download manager
data_dirs = dl_manager.download_and_extract(_URLS)  # Download and extract the data

# Define a path to save the dataset
save_path = Path("dataset.csv")  # Specify where to save the dataset locally

# Get paths for the data components (questions, annotations, images)
train_questions_path = data_dirs["questions"]["train"]
train_annotations_path = data_dirs["annotations"]["train"]
train_images_path = Path(data_dirs["images"]["train"])  # Ensure it's a valid Path object

# Create a dataset instance and generate examples
dataset = VQAv2Dataset()  # Initialize your custom dataset class

# Generate examples with the correct arguments
examples = dataset._generate_examples(
    questions_path=train_questions_path,
    annotations_path=train_annotations_path,
    images_path=train_images_path,
)

# Convert examples to a DataFrame
example_list = [item for _, item in examples]  # Extract data
df = pd.DataFrame(example_list)  # Create a pandas DataFrame

# Save the DataFrame to a CSV file
df.to_csv(save_path, index=False)  # Save without index
