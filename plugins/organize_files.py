import os
import shutil
def organize_files(files: list):
    """ 
    Organize files into corresponding folders
    """ 
    for file in files:
        if os.path.isfile(file) and file != '.DS_Store':  # Skip .DS_Store
            file_extension = os.path.splitext(file)[1] if os.path.splitext(file)[1] else 'No extension'
            folder_name = f"{file_extension.strip('.')} files"  # Folder name based on extension
            if os.path.exists(folder_name):  # If folder exists, move the file there
                shutil.move(file, os.path.join(folder_name, file))
                print(f"Moved {file} into {os.path.join(folder_name, file)} folder name {folder_name}")