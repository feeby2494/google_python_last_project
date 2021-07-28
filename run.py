#!/usr/bin//env python3

import requests
import os
import re

url = "http://localhost/fruits/"

desc_path = os.path.join(os.getcwd(), "supplier-data", "descriptions")
desc_list = os.listdir(desc_path)

image_path = os.path.join(os.getcwd(), "supplier-data", "images")
image_lists = os.listdir(image_path)



#init are dictionary for our future json

post_data_list = []

#parse through desc_list
for file in desc_list:
    file_name = os.path.splitext(file)[0].lower()
    with open(os.path.join(desc_path, file), 'r') as f:
        reader_list = f.readlines()
        json_obj = {}
        json_obj["name"] = reader_list[0].strip()
        json_obj["weight"] = int(re.sub('[^0-9]', '', reader_list[1].strip()))
        json_obj["description"] = reader_list[2].strip()
        json_obj["image_name"] = f"{file_name}.jpeg"
    post_data_list.append(json_obj)
#open and read each text file
#create the field needed and set values
#did both above


#print out object and check
#print(post_data_list)

#if okay, then post
for fruit in post_data_list:
    r = requests.post(url, data=fruit)
    print(f"for {fruit} ; status code is: {r.status_code}")

#uploading JPEGs
#for image in image_lists:
#    if os.path.splitext(image)[1].lower() == ".jpeg":
#        with open(os.path.join(image_path, image), 'rb') as opened:
#            r = requests.post(url, files={'file': opened})
#            print(f"For file: {image} ; status code is: {r.status_code}")

