import os

def load_extension(files: list):
    """
    Generate a list with all extensions in the folder
    """
    extensions = list()
    for file in files:
        if os.path.isfile(file) and file != '.DS_Store':  # Skip .DS_Store
            ext = os.path.splitext(file)[1] if os.path.splitext(file)[1] else 'No extension'
            extensions.append(ext)
    return extensions