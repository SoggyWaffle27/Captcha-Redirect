import os

def list_subfolders(main_folder_path):
    # List all entries in the main folder
    entries = os.listdir(main_folder_path)
    
    # Filter entries to include only folders
    subfolders = [entry for entry in entries if os.path.isdir(os.path.join(main_folder_path, entry))]
    
    return subfolders

main_folder_path = 'Image_Sets'
print(list_subfolders(main_folder_path))