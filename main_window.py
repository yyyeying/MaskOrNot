# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from camera import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.desktop = QtWidgets.QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenHeight = self.screenRect.height()
        self.screrenWidth = self.screenRect.width()
        self.videoWidth = 1280
        self.videoHeight = 720
        print("Desktop resolution: {}*{}".format(self.screrenWidth, self.screenHeight))
        self.scale = (self.screrenWidth/1920+self.screenHeight/1080)/2
        self.windowWidth = int(1300 * self.scale)
        self.windowHeight = int(860 * self.scale)
        print("Window size: {}*{}".format(self.windowWidth, self.windowHeight))
        print("Video resolution: {}*{}".format(self.videoWidth*self.scale, self.videoHeight*self.scale))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.windowWidth, self.windowHeight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_main = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_main.setGeometry(QtCore.QRect(0, 0, self.windowWidth - 20, self.windowHeight - 60))
        self.verticalLayoutWidget_main.setObjectName("verticalLayoutWidget_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_main)
        self.verticalLayout.setContentsMargins(10*self.scale, 10*self.scale, 10*self.scale, 10*self.scale)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_camera = QtWidgets.QLabel(self.verticalLayoutWidget_main)
        self.label_camera.setObjectName("GraphicsView_camera")
        self.label_camera.setMinimumSize(self.videoWidth*self.scale, self.videoHeight*self.scale)
        self.label_camera.setScaledContents(True)
        default_picture = QtGui.QPixmap('no_video_signal.png')
        self.label_camera.setPixmap(default_picture)
        self.verticalLayout.addWidget(self.label_camera)
        self.horizontalLayout_wear_mask = QtWidgets.QHBoxLayout()
        self.horizontalLayout_wear_mask.setObjectName("horizontalLayout_3")
        self.label_wear_mask = QtWidgets.QLabel(self.verticalLayoutWidget_main)
        font = QtGui.QFont()
        font.setPointSize(12*self.scale)
        font.setBold(True)
        font.setWeight(75)
        self.label_wear_mask.setFont(font)
        self.label_wear_mask.setObjectName("label_wear_mask")
        self.horizontalLayout_wear_mask.addWidget(self.label_wear_mask)
        self.label_yes_or_no = QtWidgets.QLabel(self.verticalLayoutWidget_main)
        font = QtGui.QFont()
        font.setPointSize(12*self.scale)
        self.label_yes_or_no.setFont(font)
        self.label_yes_or_no.setObjectName("label_yes_or_no")
        self.horizontalLayout_wear_mask.addWidget(self.label_yes_or_no)
        self.verticalLayout.addLayout(self.horizontalLayout_wear_mask)
        self.horizontalLayout_temperature = QtWidgets.QHBoxLayout()
        self.horizontalLayout_temperature.setObjectName("horizontalLayout")
        self.label_temperature = QtWidgets.QLabel(self.verticalLayoutWidget_main)
        font = QtGui.QFont()
        font.setPointSize(12*self.scale)
        font.setBold(True)
        font.setWeight(75)
        self.label_temperature.setFont(font)
        self.label_temperature.setObjectName("label_temperature")
        self.horizontalLayout_temperature.addWidget(self.label_temperature)
        self.lcdNumber_temperature = QtWidgets.QLCDNumber(self.verticalLayoutWidget_main)
        font = QtGui.QFont()
        font.setPointSize(12*self.scale)
        font.setBold(False)
        font.setWeight(50)
        self.lcdNumber_temperature.setFont(font)
        self.lcdNumber_temperature.setProperty("value", 36.5)
        self.lcdNumber_temperature.setObjectName("lcdNumber_temperature")
        self.horizontalLayout_temperature.addWidget(self.lcdNumber_temperature)
        self.verticalLayout.addLayout(self.horizontalLayout_temperature)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, self.windowWidth-20, 30*self.scale))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.capture_video()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MaskOrNot?"))
        self.label_wear_mask.setText(_translate("MainWindow", "Wear mask?"))
        self.label_yes_or_no.setText(_translate("MainWindow", "NO"))
        self.label_temperature.setText(_translate("MainWindow", "Body Temperature"))

    def capture_frame(self):
        frame = QtGui.QPixmap(self.camera.get_frame())
        frame.scaled(self.videoWidth*self.scale, self.videoHeight*self.scale)
        self.label_camera.setPixmap(frame)

    def capture_video(self):
        self.timerCamera = QtCore.QTimer()
        self.camera = camera()
        self.timerCamera.timeout.connect(self.capture_frame)
        self.timerCamera.start(1000*1/25)






