# -*- coding: utf-8 -*-
from uavClassification import *

#fname = "test_image_cubic_resample"
fname = "orthofoto_small_cubic_resample"
inputImg = "../input/" + fname + ".tif"
stretchedImg = "../input/" + fname + "_stretched.tif"

RGBImg, RGBprofile = readRaster(inputImg)
stretched = stretchHistogram(RGBImg)
writeRaster(stretchedImg, stretched, RGBprofile)


MeanShiftSmoothing(stretchedImg, "../smooth_out.tif", "../smooth_position.tif")

print("segmentation")
MeanShiftSegmentation("../smooth_out.tif", "../segmented.tif", spatialr = 16, ranger = 10)


#######################
#testing classification
#######################

segmented = "../segmented.tif"
segmentImg, segprofile = readRaster(segmented)
RGBImg, RGBprofile = readRaster(inputImg)

print("calculate stats")
ids, stats = segmentStats(segmentImg, RGBImg)

print("main script")

print("classify")
classified = segmentClustering(stats, 5, segmentImg, ids)

print("write raster")
writeRaster("../classified.tif", classified, segprofile)
