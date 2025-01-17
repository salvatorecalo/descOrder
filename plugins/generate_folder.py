import os
from typing import TextIO

def generate_folder(extension: list, log_file: TextIO):
    """
        Auxiliary function to create folders based on file extensions
    """
    try:
        for ext in extension:
            if ext == '':  # Skip empty extensions
                ext = 'No extension'  # Treat files without extension as 'No extension'
            folder_name = f"{ext.strip('.')} files"
            if not os.path.exists(folder_name):  # Avoid creating a folder if it already exists
                os.mkdir(folder_name)
                log_file.write(f"Created {folder_name} folder \n")
    except Exception as msg:
        print(f"Error creating folders: {msg}")
    log_file.write("Created all folders")
