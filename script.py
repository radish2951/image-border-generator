import os
from PIL import Image, ImageOps

def add_border(input_image_path, output_image_path, border_ratio):
    img = Image.open(input_image_path)
    border_size = (int(img.size[0] * border_ratio), int(img.size[1] * border_ratio))
    img_with_border = ImageOps.expand(img, border=border_size, fill='white')
    img_with_border.save(output_image_path)

def process_images(input_folder_path, output_folder_path, border_ratio):
    for file_name in os.listdir(input_folder_path):
        if file_name.endswith(('.jpg', '.png', '.jpeg')): # add more image extensions if needed
            input_image_path = os.path.join(input_folder_path, file_name)
            base, ext = os.path.splitext(file_name)
            output_image_path = os.path.join(output_folder_path, base + '_bordered' + ext)
            add_border(input_image_path, output_image_path, border_ratio)

process_images('input_images', 'output_images', 0.05)  # change to your folder paths and border ratio
