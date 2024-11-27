import os

def rename_images(folder_path):
    # List all files in the directory
    files = os.listdir(folder_path)
    
    # Filter only .png image files
    image_files = [f for f in files if f.lower().endswith('.png')]
    
    # Ensure there are at least 9 images
    if len(image_files) < 9:
        print("There are fewer than 9 images in the folder.")
        return
    
    # Loop through the first 9 images and rename them
    for i in range(9):
        old_name = os.path.join(folder_path, image_files[i])
        new_name = os.path.join(folder_path, f"image{i+1}.png")
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} to {new_name}")

def list_subfolders(main_folder_path):
    # List all entries in the main folder
    entries = os.listdir(main_folder_path)
    
    # Filter entries to include only folders
    subfolders = [entry for entry in entries if os.path.isdir(os.path.join(main_folder_path, entry))]
    
    return subfolders

main_folder_path = 'Input'
folders = list_subfolders('Name_Set/INPUT')
for i in folders:
    folder_path = 'Name_Set/INPUT/' + i
    rename_images(folder_path)

