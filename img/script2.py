import os
from PIL import Image

def make_images_square(input_folder, output_folder, square_size):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Skip non-image files
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Skipping non-image file: {filename}")
            continue

        try:
            # Open the image
            image = Image.open(input_path)

            # Convert to RGBA (if not already)
            image = image.convert("RGBA")

            # Get the image data
            data = image.getdata()

            # Filter out transparent pixels (alpha = 0)
            non_transparent_pixels = [pixel for pixel in data if pixel[3] > 0]

            # Get the bounding box of the non-transparent pixels
            non_transparent_image = Image.new("RGBA", image.size)
            non_transparent_image.putdata(data)

            # Get the bounding box of non-transparent pixels
            bbox = non_transparent_image.getbbox()
            if not bbox:
                print(f"No visible content in {filename}. Skipping.")
                continue

            # Crop the image to the bounding box
            cropped_image = image.crop(bbox)

            # Resize the cropped image to the desired square size
            square_image = cropped_image.resize((square_size, square_size), Image.Resampling.LANCZOS)

            # Save the final square image
            square_image.save(output_path, format="PNG")
            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Example usage
if __name__ == "__main__":
    input_folder = "img/gallery"  # Folder containing original images
    output_folder = "img/op"  # Folder to save processed images
    square_size = 500  # Desired square size (e.g., 500x500 pixels)

    make_images_square(input_folder, output_folder, square_size)
