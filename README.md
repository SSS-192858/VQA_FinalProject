# VQA_FinalProject
This is the report for the Final Mini project for the course AI-825 (Visual Recognition). This project aims to create a model for Visual Question Answering (VQA). We have done two broad approaches for the same. Both approaches use ViT as the image feature extractor and BERT as the language feature extractor. One approach involves the use of a CoTRM layer to allow cross attention between the vit and bert embeddings, and then passes them through a feed forward neural network, while the other diretly passes the embeddings through the neural network.

More details can be found in the report 

Download_Notebook.ipynb - This code is used to download the images in zip format, images and the answers in the google drive.

RandomSample.py - From the set of Images, it will sample 1/4th of the images and then store it.
QuestionSameple.py - For the images that are stored, it will pick out the corresponding questions from the questions file by matching the imageIds.
AnswerSample.py - For the question sampled, each question will have multiple answers associated with it, so it will get the answers corresponding to the same and give list of answers for that question.
