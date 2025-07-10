# QT Pyside6 Project Template

This repository will build a skeleton PySide6 project environment including a build script and the required dependencies to compile the project to executable using PyInstaller. The dependencies of this project are in requirements.txt and are installed via pip. 

It will also compile Resource and UI files for you to use.

## Compiling Resources

Qt uses a resource system that compiles files into a binary resources format. This allows you to use images and other files packaged inside your script. The `build.py` script will recursively search for files in the `./resources` directory and write them to the `Resources.qrc`. The `ui` directory is excluded from this as `ui` files usually need not be packaged into the binary. These resources will later get compiled and packaged into the executable.

In the main script the resources are imported with:

```python
import Resources
```

## Compiling UI Files

This project also contains a sample template ui file. This file is in the XML format provided by the Qt Designer. The `build.py` script will find all `./resources/*.ui` files and compile them into one python script `ui.py`. These UI components can then be imported into the main script with:

```python
from ui import *
```

Use [Qt Designer](https://www.pythonguis.com/installation/install-qt-designer-standalone/) to make custom UIs.

## First Time Use
To use:
 - Clone this repository
 - - `git clone https://github.com/chillfactor032/qt-python-project-template.git`
 - Run build.py to generate the version.json file, template ui files, and resources directories.
 - `py build.py --full`
 - - version.json has "version", "project name", "company name" that control things about the project like file names, config file locations, and window title. The field "executable" is not required, but is used to change the name of the output executable.
 - - The first time you run build.py it will generate this file.
 - - version.json has some optional fields as well:

```json
{
    "version": "1.0",
    "ico": "./resources/img/<ICON>.png",
    "company_name": "<COMPANY_NAME>",
    "product_name": "<PROJECT_NAME>",
    "description": "<PROJECT_DESCRIPTION>",
    "main_script": "MainWindow.py",
    "executable": "MyQtApp"
}
```

- Run build.py again to compile the project to executable. Note that if an icon file is specified, but doesn't exist, it will cause an error.
- - `py build.py --full`

## Partial Builds
You can also run `py build.py` with no extra arguments to only build the python part of the project but not compile it to executable. 

You can test your partial build by just executing it via python. For example, using the default MainWindow.py main script, it would be `py MainWindow.py`.

### So now what?
Create a fancy UI in Qt Designer and edit MainWindow.py to suit your project.

### Warranty

This template code is provided as is and does not carry any warranty. Refer to the LICENSE file for details. Use at your own risk. 

### Donations

Donations are appreciated but not required.

Coin | Address
--- | ---
BTC | 3C7UT1a2Do3LxFvxZt88S7gsNkRyRKXYCw
ETH | 0xc24Fc5E6C2b3E1e1eaE62f59Fab8cFBC87b1FEfc
LTC | MViPMqjn2kdMwbLAbYtgpgnHfzwwpbzUZQ