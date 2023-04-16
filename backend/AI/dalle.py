import io
import os
import cv2
import openai
import numpy as np

from .utils import read_img_from_url
from .opencv import draw_rectangle_on_image

openai.api_key = os.getenv("OPENAI_API_KEY")

def run_dalle(image, mask, prompt):
    output = openai.Image.create_edit(
        image=image,
        mask=mask,
        prompt=prompt,
        n=2,
        size="1024x1024"
    )
    return output

def get_mask(image, upper_corner, lower_corner):
    mask = draw_rectangle_on_image(image, upper_corner, lower_corner)
    return mask

def modify_image(image_url, upper_corner, lower_corner, action):
    image = read_img_from_url(image_url)
    mask = get_mask(image, upper_corner, lower_corner)
    bimage = io.BytesIO(image)
    bmask = io.BytesIO(mask)
    cv2.imwrite('datasets/a.png', bimage)
    cv2.imwrite('datasets/b.png', bmask)
    breakpoint()
    return run_dalle(bimage, bmask, action)
