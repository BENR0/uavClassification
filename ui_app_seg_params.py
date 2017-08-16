# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_app_seg_params.ui'
#
# Created: Wed Aug 16 22:56:34 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.segResult = ImageView(self.centralwidget)
        self.segResult.setEnabled(True)
        self.segResult.setMinimumSize(QtCore.QSize(600, 0))
        self.segResult.setObjectName("segResult")
        self.gridLayout.addWidget(self.segResult, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spatialr = QtWidgets.QLabel(self.centralwidget)
        self.spatialr.setObjectName("spatialr")
        self.verticalLayout.addWidget(self.spatialr)
        self.slider_spatialr = QtWidgets.QSlider(self.centralwidget)
        self.slider_spatialr.setMinimum(2)
        self.slider_spatialr.setMaximum(25)
        self.slider_spatialr.setProperty("value", 16)
        self.slider_spatialr.setOrientation(QtCore.Qt.Horizontal)
        self.slider_spatialr.setObjectName("slider_spatialr")
        self.verticalLayout.addWidget(self.slider_spatialr)
        self.ranger = QtWidgets.QLabel(self.centralwidget)
        self.ranger.setObjectName("ranger")
        self.verticalLayout.addWidget(self.ranger)
        self.slider_ranger = QtWidgets.QSlider(self.centralwidget)
        self.slider_ranger.setMinimum(2)
        self.slider_ranger.setMaximum(25)
        self.slider_ranger.setProperty("value", 10)
        self.slider_ranger.setOrientation(QtCore.Qt.Horizontal)
        self.slider_ranger.setObjectName("slider_ranger")
        self.verticalLayout.addWidget(self.slider_ranger)
        self.Numberofclasses = QtWidgets.QLabel(self.centralwidget)
        self.Numberofclasses.setObjectName("Numberofclasses")
        self.verticalLayout.addWidget(self.Numberofclasses)
        self.slider_classes = QtWidgets.QSlider(self.centralwidget)
        self.slider_classes.setMinimum(2)
        self.slider_classes.setMaximum(10)
        self.slider_classes.setProperty("value", 4)
        self.slider_classes.setOrientation(QtCore.Qt.Horizontal)
        self.slider_classes.setObjectName("slider_classes")
        self.verticalLayout.addWidget(self.slider_classes)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spatialr.setText(_translate("MainWindow", "Spatialr"))
        self.ranger.setText(_translate("MainWindow", "Ranger"))
        self.Numberofclasses.setText(_translate("MainWindow", "Number of classes"))
        self.slider_classes.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))

from pyqtgraph import ImageView
