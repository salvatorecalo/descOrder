import os
from typing import TextIO
def load_extension(files: list, log_file: TextIO, script_path: str):
    """
    Generate a list with all extensions in the folder
    """
    extensions = set()
    for file in files:
        if os.path.isfile(file) and file != '.DS_Store' and file != script_path.split("/")[-1]:  # Skip .DS_Store and main.py
            ext = os.path.splitext(file)[1] if os.path.splitext(file)[1] else 'No extension'
            extensions.add(ext)
            log_file.write(f"Added extension {ext} \n")
    return list(extensions)