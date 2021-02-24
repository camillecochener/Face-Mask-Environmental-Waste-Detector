"""
This script download the image from LabelBox using the annotation json file
Author: Camille COCHENER, 2021
"""

import os
import argparse
import json
import requests
from PIL import Image, ExifTags
from io import BytesIO


def parse_arguments():
    """
    Function to parse the arguments given in the command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('annotations_path', help='Path to the annotations json file')
    return parser.parse_args()


def download_images(args):
    """
    Function that reads the annotations json file
    """

    dir_annotations = os.path.dirname(args.annotations_path)

    with open(args.annotations_path, 'r') as f:
        annotations = json.loads(f.read()) # annotations is a list
    
    n_images = len(annotations) # number of images (65)

    for i in range(n_images):
        image_name = annotations[i]["External ID"]
        image_url = annotations[i]["Labeled Data"]

        file_path = os.path.join(dir_annotations, image_name)

        # Download the images
        if not os.path.isfile(file_path):
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img.save(file_path)


def main():
    # Parse arguments
    args = parse_arguments()
    # Download images
    download_images(args)


if __name__ == '__main__':
    main()
