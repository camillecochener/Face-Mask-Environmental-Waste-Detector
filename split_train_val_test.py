"""
This script allows to split the dataset into three parts :
- a test set with 10% of the data
- a validation set with 10% of the data
- a training set with 80% of the data
Authors: Camille COCHENER, 2021
"""

import os
import argparse
import json
import numpy as np
import requests
from PIL import Image
from io import BytesIO


def parse_arguments():
    """
    Function to parse the arguments given in the command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_folder', help='Path to the raw dataset folder')
    return parser.parse_args()


def split_dataset(args):
    """
    Function to read the annotations and to get the number of images for each part
    """
    path_to_annnotations = os.path.join(args.dataset_folder, 'annotations.json')
    
    with open(path_to_annnotations, 'r') as f:
        data = json.loads(f.read())
    
    n_images = len(data)

    # Split the dataset
    train, validate, test = np.split(data, [int(len(data)*0.8), int(len(data)*0.9)])
    train, validate, test = list(train), list(validate), list(test)

    # Create folder
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")

    path_to_new_folder = "dataset" 
    
    list_folder = ["train", "val", "test"]
    for i in list_folder:
        if not os.path.isdir(os.path.join("dataset", i)):
            os.mkdir(os.path.join("dataset", i))
        annot_path = os.path.join("dataset", i, 'annotations.json')
        if not os.path.isfile(annot_path):
            if i == 'train':
                with open(annot_path, 'w+') as f:
                    f.write(json.dumps(train))
            if i == 'val':
                with open(annot_path, 'w+') as f:
                    f.write(json.dumps(validate))
            if i == 'test':
                with open(annot_path, 'w+') as f:
                    f.write(json.dumps(test))
    return train, validate, test


def get_images(train, validate, test):
    """
    Function to download the images for each part of the dataset
    """
    n_images = [len(train), len(validate), len(test)]
    list_folder = ["train", "val", "test"]
    subset = [train, validate, test]

    for k, folder in enumerate(list_folder):
        for i in range(n_images[k]):
            image_name = subset[k][i]["External ID"]
            image_url = subset[k][i]["Labeled Data"]

            file_path = os.path.join("dataset", folder, image_name)

            # Download the images
            if not os.path.isfile(file_path):
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                img.save(file_path)


def main():
    # Parse arguments
    args = parse_arguments()
    # Split the dataset
    train, validate, test = split_dataset(args)
    # Download images
    get_images(train, validate, test)

if __name__ == '__main__':
    main()