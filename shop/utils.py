import os
import requests
import base64

def upload_image_to_imgbb(image_path, api_key):
    url = "https://api.imgbb.com/1/upload"
    with open(image_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')
    payload = {
        "key": api_key,
        "image": encoded_string,
    }
    response = requests.post(url, payload)
    json_response = response.json()
    if "data" in json_response:
        image_url = json_response["data"]["url"]
        os.remove(image_path)
        return image_url



