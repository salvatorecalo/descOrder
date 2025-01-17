"""
 Copyright Salvatore Calo
 License GNU 3.0
 Version 1.0

 Order all file in a folder in subfolder based on the type
"""
import os
from plugins.load_extension import load_extension
from plugins.generate_folder import generate_folder
from plugins.organize_files import organize_files
import sys 

def main():
    if getattr(sys, 'frozen', False):
        os.chdir(os.path.dirname(sys.executable))
        script_path = os.path.abspath(__file__)
    else:
        os.chdir(os.path.dirname(__file__))
        script_path = os.path.abspath(__file__)
    with open(f"{os.path.curdir}/log_file.txt", "w") as log_file:
        print("log file created")
        files = os.listdir()
        extension = load_extension(files, log_file, script_path)
        generate_folder(extension, log_file)
        organize_files(files, script_path, log_file)
main()