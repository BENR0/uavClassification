# -*- coding: utf-8 -*-
from uavClassification import *

#fname = "test_image_cubic_resample"
fname = "orthofoto_small_cubic_resample"
inputImg = "../input/" + fname + ".tif"
stretchedImg = "../input/" + fname + "_stretched.tif"

RGBImg, RGBprofile = readRaster(inputImg)
stretched = stretchHistogram(RGBImg)
writeRaster(stretchedImg, stretched, RGBprofile)


MeanShiftSmoothing(stretchedImg, "../output/smooth/smooth_out.tif", "../output/smooth_position.tif")

print("segmentation")
MeanShiftSegmentation("../output/smooth/smooth_out.tif", "../output/segmented/segmented.tif", spatialr = 16, ranger = 10)


#######################
#testing classification
#######################

segmented = "../output/segmented/segmented.tif"
segmentImg, segprofile = readRaster(segmented)
RGBImg, RGBprofile = readRaster(stretchedImg)

print("calculate stats")
ids, stats = segmentStats(segmentImg, RGBImg)

print("main script")

print("classify")
classified = segmentClustering(stats, 5, segmentImg, ids)

print("write raster")
writeRaster("../output/classified/classified.tif", classified, segprofile)
