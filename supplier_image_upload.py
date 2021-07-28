#!//usr/bin//env python3

import requests
import os

url = "http://localhost/upload/"

image_path = os.path.join(os.getcwd(), "supplier-data", "images")
image_lists = os.listdir(image_path)

#cleaning up non-JPEG files inside of image_lists
for image in image_lists:
    if "README" in image or "LICENSE" in image:
        image_lists.remove(image)
    if os.path.splitext(image)[1].lower() is ".tiff":
        image_lists.remove(image)


#uploading JPEGs
for image in image_lists:
    if os.path.splitext(image)[1].lower() == ".jpeg":
        with open(os.path.join(image_path, image), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(f"For file: {image} ; status code is: {r.status_code}")
