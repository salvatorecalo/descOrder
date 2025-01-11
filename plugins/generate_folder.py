import os

def generate_folders(extension: list):
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
                print(f"Created {folder_name} folder")
    except Exception as msg:
        print(f"Error creating folders: {msg}")
    print("Created all folders")
