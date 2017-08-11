# -*- coding: utf-8 -*-
from uavClassification import *

inputImg = "../orthofoto_small_cubic_resample.tif"

#MeanShiftSmoothing(inputImg, "../smooth_out.tif", "../smooth_position.tif")

#print("segmentation")
#MeanShiftSegmentation("../smooth_out.tif", "../segmented.tif")

#print("colormapping")
#colorMapping("../segmented.tif", "../labeled.tif")


print("numpy")
smoothed = MeanShiftSmoothing(inputImg, "test.tif", "test.tif", outnp = True)

print("segmentation")

segmented = MeanShiftSegmentation(smoothed, "test.tif", innp = True, outnp = True)

print("colormapping")
colorMapping(segmented, "../labeled_np.tif", innp = True)
