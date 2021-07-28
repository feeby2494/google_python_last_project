#!/usr/bin/env python3

import os
from PIL import Image

image_path = os.path.join(os.getcwd(), "supplier-data", "images")
images_list = os.listdir(image_path)
output_dir = image_path

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

if ".DS_Store" in images_list:
    images_lists.remove(".DS_Store")
if "README" in images_list:
    images_list.remove("README")

if "LICENSE" in images_list:
    images_list.remove("LICENSE")

for image in images_list:
    image_name = os.path.splitext(image)[0]
    with Image.open(os.path.join(image_path, image)) as im:
        im.convert('RGB').resize((600, 400)).save(f"{os.path.join(output_dir)}/{image_name}.jpeg", "JPEG" )

