"""
 Copyright Salvatore Calo
 License GNU 3.0
 Version 1.0

 Order all file in a folder in subfolder based on the type
"""
import os
from plugins.load_extension import load_extension
from plugins.generate_folder import generate_folders
from plugins.organize_files import organize_files

def main():
    files = os.listdir()
    extension = load_extension(files)
    generate_folders(extension)
    organize_files(files)
    
main()