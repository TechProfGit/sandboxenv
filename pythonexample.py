#Read a first directory in a folder
import os

def get_first_folder(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            return item
    return None  # No folder found

directory_path = '/path/to/your/directory'

first_folder = get_first_folder(directory_path)

if first_folder:
    print("First folder name:", first_folder)
else:
    print("No folders found in the directory.")
