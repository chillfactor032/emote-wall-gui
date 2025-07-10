# Python Imports
import sys
import json
import os
import time
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle
from PySide6.QtCore import QSettings, QFile, QTextStream, QStandardPaths, QSize
from PySide6.QtGui import QPixmap, QIcon, QPalette, QColor

# Import resources and UI components
import Resources_rc
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
            os.makedirs(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"{self.project_name}.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

        # Variables
        self._LEFT = -1
        self._RIGHT = 1
        self.delay_secs = int(self.settings.value("delay_secs", "10"))
        self.emote_buffer_size = int(self.settings.value("emote_buffer_size", "15"))
        self.twitch_channel_name = self.settings.value("twitch_channel_name", "")
        self.twitch_api_key = self.settings.value("twitch_bot_api_key", "")
        self.display_mode = self.settings.value("display_mode", "Auto Cycle")

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        pc_icon_pixmap = QPixmap(":resources/img/pc_icon.ico")
        pc_icon = QIcon(pc_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)
        
        # Get Icons
        self.grid_icon_pixmap = QPixmap(":resources/img/icons/grid.svg")
        self.grid_icon_pixmap.scaledToHeight(40)
        self.grid_icon_pixmap.scaledToWidth(40)
        self.grid_icon = QIcon(self.grid_icon_pixmap)
        self.eye_icon_pixmap = QPixmap(":resources/img/icons/eye.svg")
        self.eye_icon = QIcon(self.eye_icon_pixmap)

        #Setup Button Signals
        # Button/Menu Signals Go Here
        self.save_button.clicked.connect(self.save_clicked)
        self.preview_screen_button.clicked.connect(self.preview_button_clicked)
        self.delay_left_button.clicked.connect(lambda : self.modify_delay(self._LEFT))
        self.delay_right_button.clicked.connect(lambda : self.modify_delay(self._RIGHT))
        self.buffer_left_button.clicked.connect(lambda : self.modify_buffer(self._LEFT))
        self.buffer_right_button.clicked.connect(lambda : self.modify_buffer(self._RIGHT))
        self.mode_combo.currentIndexChanged.connect(self.mode_combo_clicked)
        self.cycle_left_button.clicked.connect(lambda : self.cycle_button_clicked(self._LEFT))
        self.cycle_right_button.clicked.connect(lambda : self.cycle_button_clicked(self._RIGHT))

        #Set UI Fields
        self.stacked_widget.setCurrentIndex(0)
        self.delay_lcd.display(str(self.delay_secs))
        self.buffer_lcd.display(str(self.emote_buffer_size))
        self.twitch_channel_input.setText(self.twitch_channel_name)
        mode_index = self.mode_combo.findText(self.display_mode)
        if mode_index == -1:
            self.mode_combo.setCurrentIndex(0)
            self.display_mode = self.mode_combo.currentText()
        else:
            self.mode_combo.setCurrentIndex(mode_index)
        self.mode_combo_clicked()
        self.save_button.setFocus()
        
        #Finally, Show the UI
        geometry = self.settings.value(f"{self.project_name}/geometry")
        window_state = self.settings.value(f"{self.project_name}/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.show()

    def cycle_button_clicked(self, direction):
        if direction >= 0:
            print("Cycle Right")
        else:
            print("Cycle Left")

    def mode_combo_clicked(self):
        self.display_mode = self.mode_combo.currentText()
        if self.display_mode != "Auto Cycle":
            self.delay_left_button.setDisabled(True)
            self.delay_right_button.setDisabled(True)
            self.delay_lcd.setDisabled(True)
        else:
            self.delay_lcd.setDisabled(False)
            self.delay_left_button.setDisabled(False)
            self.delay_right_button.setDisabled(False)

    def save_clicked(self):
        self.delay_secs = self.delay_lcd.intValue()
        self.emote_buffer_size = self.buffer_lcd.intValue()
        self.twitch_channel_name = self.twitch_channel_input.text()
        self.display_mode = self.mode_combo.currentText()
        self.save_fields()

    def save_fields(self):
        self.settings.setValue("delay_secs", str(self.delay_secs))
        self.settings.setValue("emote_buffer_size", str(self.emote_buffer_size))
        self.settings.setValue("twitch_channel_name", str(self.twitch_channel_name))
        self.settings.setValue("twitch_bot_api_key", str(self.twitch_api_key))
        self.settings.setValue("display_mode", str(self.display_mode))
        self.settings.sync()

    def modify_delay(self, amount=0):
        self.delay_secs += amount
        if self.delay_secs < 1:
            self.delay_secs = 1
        self.delay_lcd.display(str(self.delay_secs))

    def modify_buffer(self, amount=0):
        self.emote_buffer_size += amount
        if self.emote_buffer_size < 1:
            self.emote_buffer_size = 1
        self.buffer_lcd.display(str(self.emote_buffer_size))

    def preview_button_clicked(self):
        cur = (self.stacked_widget.currentIndex() + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(cur)
        if self.stacked_widget.currentWidget() == self.preview_widget:
            self.preview_screen_button.setIcon(self.grid_icon)
        else:
            self.preview_screen_button.setIcon(self.eye_icon)
        self.preview_screen_button.setIconSize(QSize(40,40))

    # App is closing, cleanup
    def closeEvent(self, evt):
        # Save values
        self.save_fields()

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
    app.setPalette(QPalette(QColor("#19171D")))
    app.setStyle("Fusion")
    window = MainWindow()
    sys.exit(app.exec())
