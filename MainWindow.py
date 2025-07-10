# Python Imports
import sys
import json
import os
import time
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle
from PySide6.QtCore import QSettings, QFile, QTextStream, QStandardPaths
from PySide6.QtGui import QPixmap, QIcon

# Import resources and UI components
import Resources
from ui import *

#Log Levels
class LogLevel(Enum):
    INFO = 0
    ERROR = 10
    DEBUG = 20
    
    @staticmethod
    def get(value):
        for level in LogLevel:
            if(value == level.value):
                return level
        return LogLevel.INFO


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        #Load UI Components
        self.setupUi(self)
        
        #Read Version File From Resources
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        self.project_name = self.app_name.title().replace(" ", "")
        self.setWindowTitle(f"{self.app_name} {self.version}")
        
        #Load Settings
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        if(not os.path.isdir(self.config_dir)):
            os.mkdir(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"{self.project_name}.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        pc_icon_pixmap = QPixmap(":resources/img/pc_icon.ico")
        pc_icon = QIcon(pc_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)
        
        #Setup Button Signals
        # Button/Menu Signals Go Here
        
        #Finally, Show the UI
        geometry = self.settings.value(f"{self.project_name}/geometry")
        window_state = self.settings.value(f"{self.project_name}/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.show()

    # App is closing, cleanup
    def closeEvent(self, evt):
        # Remember the size and position of the GUI
        self.settings.setValue(f"{self.project_name}/geometry", self.saveGeometry())
        self.settings.setValue(f"{self.project_name}/windowState", self.saveState())
        self.settings.sync()
        evt.accept()

# Start the PySide6 App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    version_file = QFile(":version.json")
    version_file.open(QFile.ReadOnly)
    text_stream = QTextStream(version_file)
    version_file_text = text_stream.readAll()
    version_dict = json.loads(version_file_text)
    org_name = version_dict["company_name"]
    app_name = version_dict["product_name"]
    version = version_dict["version"]
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    window = MainWindow()
    sys.exit(app.exec())