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
        #self.segResult.addItem(pyqtgraph.ImageItem())


    def runSegment(self):
        slSpatialr = self.slider_spatialr.value()
        slRanger = self.slider_ranger.value()
        slClasses = self.slider_classes.value()

        RGBinput = "../input/test_image_cubic_resample.tif" 
        segmentedout = "../output/segmented/app_segmented.tif"
        smoothed = "../output/smooth/smoothed.tif"


        MeanShiftSegmentation(smoothed, segmentedout, spatialr = slSpatialr, ranger = slRanger)

        segmentedImg, segprofile = readRaster(segmentedout)
        RGBImg, rgbgrofile = readRaster(RGBinput)


        ids, stats = segmentStats(segmentedImg, RGBImg)
        classified = segmentClustering(stats, slClasses, segmentedImg, ids)


        self.segResult.setImage(classified)


    def runClassification(self):
        slClasses = self.slider_classes.value()

        RGBinput = "../input/test_image_cubic_resample.tif" 
        segmentedout = "../output/segmented/app_segmented.tif"

        RGBImg, rgbgrofile = readRaster(RGBinput)
        segmentedImg, segprofile = readRaster(segmentedout)


        ids, stats = segmentStats(segmentedImg, RGBImg)
        classified = segmentClustering(stats, slClasses, segmentedImg, ids)


        self.segResult.setImage(classified)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = segmentationParams()
    form.show()
    form.runSegment()
    app.exec_()
