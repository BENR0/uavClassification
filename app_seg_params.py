from PyQt5 import QtGui, QtWidgets
import sys
import numpy as np
import pyqtgraph
from uavClassification import *

import ui_app_seg_params


class segmentationParams(QtGui.QMainWindow, ui_app_seg_params.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOptions(imageAxisOrder='row-major')
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.slider_spatialr.valueChanged.connect(self.runSegment)
        self.slider_ranger.valueChanged.connect(self.runSegment)
        self.slider_classes.valueChanged.connect(self.runClassification)
        self.imageItem = pyqtgraph.ImageItem()
        self.view = pyqtgraph.ViewBox()
        self.view.addItem(self.imageItem)
        #segResult is of class pyqtgraph.GraphicsView
        self.segResult.setCentralItem(self.view)

        #get file pathes with buttons
        self.RGBimgpathButton.clicked.connect(self.getFileRGB)
        self.smoothedpathButton.clicked.connect(self.getFilesmoothed)
        self.segmentedout = "../output/segmented/app_segmented.tif"

        self.RGBimgpath = "../input/test_image_cubic_resample.tif" 
        self.smoothedpath = ""
        #smoothed = "../output/smooth/smoothed.tif"
        

    def getFileRGB(self):
        self.RGBimgpath = str(QtWidgets.QFileDialog.getOpenFileName(self, "Open RGB file", "~")[0])
        self.RGBimgpathlabel.setText(self.RGBimgpath)

    def getFilesmoothed(self):
        self.smoothedpath = str(QtWidgets.QFileDialog.getOpenFileName(self, "Open smoothed file", "~")[0])
        self.smoothedpathlabel.setText(self.smoothedpath)

    def runSegment(self):
        slSpatialr = self.slider_spatialr.value()
        slRanger = self.slider_ranger.value()
        slClasses = self.slider_classes.value()

        mssin = self.smoothedpath
        mssout = self.segmentedout

        MeanShiftSegmentation(mssin, mssout, spatialr = slSpatialr, ranger = slRanger)

        segmentedImg, segprofile = readRaster(self.segmentedout)
        RGBImg, rgbgrofile = readRaster(self.RGBimgpath)


        ids, stats = segmentStats(segmentedImg, RGBImg)
        classified = segmentClustering(stats, slClasses, segmentedImg, ids)


        self.imageItem.setImage(classified[0])


    def runClassification(self):
        slClasses = self.slider_classes.value()


        RGBImg, rgbgrofile = readRaster(self.RGBimgpath)
        segmentedImg, segprofile = readRaster(self.segmentedout)


        ids, stats = segmentStats(segmentedImg, RGBImg)
        classified = segmentClustering(stats, slClasses, segmentedImg, ids)


        self.imageItem.setImage(classified[0])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = segmentationParams()
    form.show()
    #form.runSegment()
    app.exec_()
