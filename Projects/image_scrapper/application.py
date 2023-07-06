import requests
from bs4 import BeautifulSoup
import logging
import os
import json

# Initialize a directory to store scrapped images
image_dir = "scrped_images/"

# Headers to avoid getting blocked by server
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# Check if the directory exists, if not create a directory
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

query = "AI generated Modi Photos".replace(" ", "+")
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M", headers = headers)

soup = BeautifulSoup(response.content, "html.parser")
image_tags = soup.find_all("img", {"class" : "yWs4tf"})
# print(image_tags)

image_json = []

for image in image_tags:
    source = image["src"]
    image_data = requests.get(source).content
    with open(os.path.join(image_dir, f"{query}_{image_tags.index(image)}.jpg"), "wb") as image_file:
        image_file.write(image_data)
    image_dict = {'key' : source, 'data' : image_data}
    print(image_dict)
    image_json.append(image_dict)

