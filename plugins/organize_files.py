import os
import shutil
from typing import TextIO
def organize_files(files: list, script_path: str, log_file: TextIO):
    """ 
    Organize files into corresponding folders
    """ 
    for file in files:
        file_path = os.path.abspath(file)
        if os.path.isfile(file) and file != '.DS_Store' and file_path != script_path:  # Skip .DS_Store
            file_extension = os.path.splitext(file)[1] if os.path.splitext(file)[1] else 'No extension'
            folder_name = f"{file_extension.strip('.')} files"  # Folder name based on extension
            if os.path.exists(folder_name):  # If folder exists, move the file there
                shutil.move(file, os.path.join(folder_name, file))
                log_file.write(f"Moved {file} into {os.path.join(folder_name, file)} folder name {folder_name} \n")