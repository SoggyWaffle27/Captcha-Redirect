from PIL import Image
import os

def split_image(filepath, runs):
    # Open the original image
    original_image = Image.open(filepath)
    width, height = original_image.size

    # Calculate dimensions for the smaller images
    small_width = width // 3
    small_height = height // 3

    # Create a directory to save the smaller images
    output_dir = "output_images" + str(runs)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Crop and save the 9 smaller images
    for i in range(3):
        for j in range(3):
            left = j * small_width
            upper = i * small_height
            right = (j + 1) * small_width
            lower = (i + 1) * small_height
            cropped_image = original_image.crop((left, upper, right, lower))
            cropped_image.save(os.path.join(output_dir, f"image{i * 3 + j + 1}.png"))

def list_images(folder_path):
    # List all entries in the folder
    entries = os.listdir(folder_path)
    
    # Filter entries to include only image files
    image_extensions = ('.png')
    images = [entry for entry in entries if entry.lower().endswith(image_extensions)]
    
    return images

imgs = list_images('Image_Spliter/INPUT')
runs = 0
for i in imgs:
    runs += 1
    image_path = 'Image_Spliter/INPUT/' + i
    split_image(image_path, runs)

# Example single usage
# Split_image("Image Spliter/crosswalks.png")
