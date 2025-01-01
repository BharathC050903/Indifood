#This script was written to: Resize images with padding

import os
from PIL import Image

def add_padding_to_folder(input_folder, output_folder, target_width, target_height):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Skip non-image files
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        # Open the image
        try:
            image = Image.open(input_path)
        except Exception as e:
            print(f"Skipping {filename}: {e}")
            continue

        # Calculate padding
        left = (target_width - image.width) // 2
        top = (target_height - image.height) // 2
        right = target_width - image.width - left
        bottom = target_height - image.height - top

        # Create a new image with a transparent background
        new_image = Image.new("RGB", (target_width, target_height), (96, 89, 79))
        
        # Paste the original image onto the new image
        new_image.paste(image, (left, top))
        
        # Save the result
        new_image.save(output_path, format="PNG")
        print(f"Processed: {filename}")

# Example usage
input_folder = "img/customers"
output_folder = "img/op"
target_width = 500
target_height = 500

add_padding_to_folder(input_folder, output_folder, target_width, target_height)
