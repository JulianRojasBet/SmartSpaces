import base64
import os
import requests
from PIL import Image
from pprint import pprint
import string
import random
import io

engine_id = "stable-diffusion-xl-beta-v2-2-2"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY","sk-OMLvfTP6jC94KTMqSwfK4BAPgXWesyqO7Sv94lz5YcWp20Wi")

def list_engines():
    url = f"{api_host}/v1/engines/list"
    response = requests.get(url, headers={
        "Authorization": f"Bearer {api_key}"
    })
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    # Do something with the payload...
    payload = response.json()
    pprint(payload)

def resize_image(image):
    width, height = image.size
    while width * height > (512*512):
        width = int(width / 2)
        height = int(height / 2)
    
    new_width = int(width / 64) * 64
    new_height = int(height / 64) * 64

    resized_image = image.resize((new_width, new_height))
    buffer = io.BytesIO()
    resized_image.save(buffer, format='JPEG')
    buffer.seek(0)
    return buffer

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def read_img_from_url(url): 
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content))
    resized_img_str = resize_image(img)
    return resized_img_str

def modify(url, suggestion):
    image = read_img_from_url(url)
    image_name = f"{generate_random_string(20)}"
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/image-to-image",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        files={
            "init_image": image
        },
        data={
            "image_strength": 0.80,
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": suggestion,
            "cfg_scale": 10,
            "clip_guidance_preset": "NONE",
            "samples": 1,
            "steps": 80,
        }
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    result_paths = []
    for i, image in enumerate(data["artifacts"]):
        out_path = f"AI/out/{image_name}_{i}.png"
        with open(out_path, "wb") as f:
            f.write(base64.b64decode(image["base64"]))
        result_paths.append(out_path)
    return result_paths


if __name__ == "__main__":
    list_engines()
    modify("https://a0.muscache.com/im/pictures/miso/Hosting-33996825/original/50993bdb-b05b-4096-9b67-740447719a62.jpeg?im_w=1200", "add a security camara to the wall of the room, on the upper left corner")