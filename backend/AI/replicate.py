import replicate

# Models
stable_diffusion = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478"
replicate_resnet = "replicate/resnet:dd782a3d531b61af491d1026434392e8afb40bfb53b8af35f727e80661489767"
pixray_text2img = "pixray/text2image:5c347a4bfa1d4523a58ae614c2194e15f2ae682b57e3797a5bb468920aa70ebf"
instruct_pix2pix = "timothybrooks/instruct-pix2pix:30c1d0b916a6f8efce20493f5d61ee27491ab2a60437c13c588468b9810ec23f"


def modify_image(image_url, prompt):
    output = replicate.run(
        instruct_pix2pix,
        input={
            "image": image_url,
            "prompt": prompt,
        }
    )
    return output
