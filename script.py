# -*- coding: utf-8 -*-
from uavClassification import *

inputImg = "../test_image_cubic_resample.tif"

#MeanShiftSmoothing(inputImg, "../smooth_out.tif", "../smooth_position.tif")

#print("segmentation")
#MeanShiftSegmentation("../smooth_out.tif", "../segmented.tif")

#print("colormapping")
#colorMapping("../segmented.tif", "../labeled.tif")


#print("numpy")
#smoothed = MeanShiftSmoothing(inputImg, None, None, outnp = True)

#print("segmentation")
#segmented = MeanShiftSegmentation(smoothed, None,  innp = True, outnp = True)

#print("colormapping")
#colorMapping(segmented, "../labeled_np.tif", innp = True)


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
