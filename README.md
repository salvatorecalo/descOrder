# Fastly organize messy files in a folder with this Python script


## Create your virtual environment
```
python -m venv
```

### Note: Ensure you specify the name venv for the virtual environment when running the command.

## Activate the virtual environment
* Linux/Macos
```
source venv/bin/activate
```
* Windows (cmd):
```
venv\Scripts\activate
```
* Windows (PowerShell): powershell

```
.\venv\Scripts\Activate
```
## Install PyInstaller
### Install PyInstaller using pip:

```
pip install pyinstaller
```

## Generate the Executable
### Use PyInstaller to create a single executable file:
```
<<<<<<< HEAD
pyinstaller --onefile --noconsole main.py
=======
pyinstaller --onefile --noconsole script.py
>>>>>>> 3f7e5c8 (Create README.md)
```

### **NB: The executable will be placed inside the dist folder.**

## Move the Executable to the Desired Folder
<<<<<<< HEAD

## If you're on macOs/linux give the permission
```
chmod +x main
```
=======
>>>>>>> 3f7e5c8 (Create README.md)
### Copy or move the .exe file from the dist folder to the directory you want to organize.

## Run the Executable
### Double-click the ```.exe``` file to organize the files in the folder.
