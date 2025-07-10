# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(320, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.widget_9 = QWidget(self.groupBox_2)
        self.widget_9.setObjectName(u"widget_9")
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.widget_9.setFont(font)
        self.formLayout = QFormLayout(self.widget_9)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, -1, 6, -1)
        self.widget_4 = QWidget(self.widget_9)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/resources/img/icons/twitch.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.widget_4)

        self.widget_6 = QWidget(self.widget_9)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.twitch_channel_input = QLineEdit(self.widget_6)
        self.twitch_channel_input.setObjectName(u"twitch_channel_input")
        self.twitch_channel_input.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setPointSize(13)
        self.twitch_channel_input.setFont(font2)
        self.twitch_channel_input.setEchoMode(QLineEdit.Normal)

        self.gridLayout_4.addWidget(self.twitch_channel_input, 0, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.widget_6)

        self.widget_8 = QWidget(self.widget_9)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(30, 30))
        self.label_6.setMaximumSize(QSize(30, 30))
        self.label_6.setPixmap(QPixmap(u":/resources/img/icons/smile.svg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_7)


        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.widget_8)

        self.widget_7 = QWidget(self.widget_9)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buffer_left_button = QToolButton(self.widget_7)
        self.buffer_left_button.setObjectName(u"buffer_left_button")
        self.buffer_left_button.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/resources/img/icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buffer_left_button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.buffer_left_button)

        self.buffer_lcd = QLCDNumber(self.widget_7)
        self.buffer_lcd.setObjectName(u"buffer_lcd")
        self.buffer_lcd.setMinimumSize(QSize(0, 40))
        self.buffer_lcd.setFrameShape(QFrame.Box)
        self.buffer_lcd.setLineWidth(1)
        self.buffer_lcd.setMidLineWidth(0)
        self.buffer_lcd.setDigitCount(2)
        self.buffer_lcd.setProperty("intValue", 30)

        self.horizontalLayout_5.addWidget(self.buffer_lcd)

        self.buffer_right_button = QToolButton(self.widget_7)
        self.buffer_right_button.setObjectName(u"buffer_right_button")
        self.buffer_right_button.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/resources/img/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buffer_right_button.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.buffer_right_button)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.widget_7)

        self.widget_12 = QWidget(self.widget_9)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.widget_12)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(30, 30))
        self.label_11.setMaximumSize(QSize(30, 30))
        self.label_11.setPixmap(QPixmap(u":/resources/img/icons/monitor.svg"))

        self.horizontalLayout_9.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_12)


        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.widget_12)

        self.widget_13 = QWidget(self.widget_9)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_5 = QGridLayout(self.widget_13)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mode_combo = QComboBox(self.widget_13)
        self.mode_combo.addItem("")
        self.mode_combo.addItem("")
        self.mode_combo.addItem("")
        self.mode_combo.setObjectName(u"mode_combo")
        self.mode_combo.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setPointSize(16)
        self.mode_combo.setFont(font3)

        self.gridLayout_5.addWidget(self.mode_combo, 0, 0, 1, 1)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.widget_13)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(30, 30))
        self.label_8.setMaximumSize(QSize(30, 30))
        self.label_8.setPixmap(QPixmap(u":/resources/img/icons/clock.svg"))

        self.horizontalLayout_7.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_9)


        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.delay_left_button = QToolButton(self.widget_11)
        self.delay_left_button.setObjectName(u"delay_left_button")
        self.delay_left_button.setMinimumSize(QSize(40, 40))
        self.delay_left_button.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.delay_left_button)

        self.delay_lcd = QLCDNumber(self.widget_11)
        self.delay_lcd.setObjectName(u"delay_lcd")
        self.delay_lcd.setMinimumSize(QSize(0, 40))
        self.delay_lcd.setFrameShape(QFrame.Box)
        self.delay_lcd.setLineWidth(1)
        self.delay_lcd.setMidLineWidth(0)
        self.delay_lcd.setDigitCount(2)
        self.delay_lcd.setProperty("intValue", 10)

        self.horizontalLayout_6.addWidget(self.delay_lcd)

        self.delay_right_button = QToolButton(self.widget_11)
        self.delay_right_button.setObjectName(u"delay_right_button")
        self.delay_right_button.setMinimumSize(QSize(40, 40))
        self.delay_right_button.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.delay_right_button)


        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.widget_11)


        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.widget_9)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 100))
        self.groupBox_3.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cycle_left_button = QToolButton(self.groupBox_3)
        self.cycle_left_button.setObjectName(u"cycle_left_button")
        self.cycle_left_button.setMinimumSize(QSize(50, 50))
        self.cycle_left_button.setIcon(icon)
        self.cycle_left_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.cycle_left_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.preview_screen_button = QToolButton(self.groupBox_3)
        self.preview_screen_button.setObjectName(u"preview_screen_button")
        self.preview_screen_button.setMinimumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/resources/img/icons/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.preview_screen_button.setIcon(icon2)
        self.preview_screen_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.preview_screen_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.cycle_right_button = QToolButton(self.groupBox_3)
        self.cycle_right_button.setObjectName(u"cycle_right_button")
        self.cycle_right_button.setMinimumSize(QSize(50, 50))
        self.cycle_right_button.setIcon(icon1)
        self.cycle_right_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.cycle_right_button)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(421, 0))
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 9, 0)
        self.stacked_widget = QStackedWidget(self.widget_2)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.preview_widget = QWidget()
        self.preview_widget.setObjectName(u"preview_widget")
        self.gridLayout_2 = QGridLayout(self.preview_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.preview_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(427, 0))
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.preview_emote_label = QLabel(self.groupBox)
        self.preview_emote_label.setObjectName(u"preview_emote_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.preview_emote_label.sizePolicy().hasHeightForWidth())
        self.preview_emote_label.setSizePolicy(sizePolicy1)
        self.preview_emote_label.setPixmap(QPixmap(u":/resources/img/lul.png"))
        self.preview_emote_label.setScaledContents(True)
        self.preview_emote_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.preview_emote_label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stacked_widget.addWidget(self.preview_widget)
        self.emote_select_widget = QWidget()
        self.emote_select_widget.setObjectName(u"emote_select_widget")
        self.gridLayout_3 = QGridLayout(self.emote_select_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.select_emote_panel = QGroupBox(self.emote_select_widget)
        self.select_emote_panel.setObjectName(u"select_emote_panel")
        self.gridLayout_7 = QGridLayout(self.select_emote_panel)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.toolButton_16 = QToolButton(self.select_emote_panel)
        self.toolButton_16.setObjectName(u"toolButton_16")
        icon3 = QIcon()
        icon3.addFile(u":/resources/img/lul.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_16.setIcon(icon3)
        self.toolButton_16.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_16, 0, 0, 1, 1)

        self.toolButton_14 = QToolButton(self.select_emote_panel)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setIcon(icon3)
        self.toolButton_14.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_14, 0, 1, 1, 1)

        self.toolButton_15 = QToolButton(self.select_emote_panel)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setIcon(icon3)
        self.toolButton_15.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_15, 0, 2, 1, 1)

        self.toolButton_11 = QToolButton(self.select_emote_panel)
        self.toolButton_11.setObjectName(u"toolButton_11")
        self.toolButton_11.setIcon(icon3)
        self.toolButton_11.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_11, 1, 0, 1, 1)

        self.toolButton_12 = QToolButton(self.select_emote_panel)
        self.toolButton_12.setObjectName(u"toolButton_12")
        self.toolButton_12.setIcon(icon3)
        self.toolButton_12.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_12, 1, 1, 1, 1)

        self.toolButton_8 = QToolButton(self.select_emote_panel)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setIcon(icon3)
        self.toolButton_8.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_8, 1, 2, 1, 1)

        self.toolButton_10 = QToolButton(self.select_emote_panel)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setIcon(icon3)
        self.toolButton_10.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_10, 2, 0, 1, 1)

        self.toolButton_13 = QToolButton(self.select_emote_panel)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setIcon(icon3)
        self.toolButton_13.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_13, 2, 1, 1, 1)

        self.toolButton_9 = QToolButton(self.select_emote_panel)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setIcon(icon3)
        self.toolButton_9.setIconSize(QSize(96, 96))

        self.gridLayout_7.addWidget(self.toolButton_9, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.select_emote_panel, 0, 0, 1, 1)

        self.stacked_widget.addWidget(self.emote_select_widget)

        self.gridLayout.addWidget(self.stacked_widget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.twitch_channel_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Channel Name", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Buffer Size", None))
        self.buffer_left_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.buffer_right_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.mode_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Auto Cycle", None))
        self.mode_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Last", None))
        self.mode_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Manual", None))

        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.delay_left_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.delay_right_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.cycle_left_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.preview_screen_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.cycle_right_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.preview_emote_label.setText("")
        self.select_emote_panel.setTitle(QCoreApplication.translate("MainWindow", u"Select Emote (1/3)", None))
        self.toolButton_16.setText("")
        self.toolButton_14.setText("")
        self.toolButton_15.setText("")
        self.toolButton_11.setText("")
        self.toolButton_12.setText("")
        self.toolButton_8.setText("")
        self.toolButton_10.setText("")
        self.toolButton_13.setText("")
        self.toolButton_9.setText("")
    # retranslateUi



