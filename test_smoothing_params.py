# -*- coding: utf-8 -*-
from uavClassification import *
from tqdm import tqdm
import itertools

inputImg = "../input/test_image_cubic_resample.tif"
RGBImg, RGBprofile = readRaster(inputImg)

radio = range(2, 18, 2)
spatial = range(2, 18, 2)
combs = itertools.product(spatial, radio)

smoothout = "../output/smooth/smoothed.tif" # "../smooth/smooth_" + run
MeanShiftSmoothing(inputImg, smoothout, "../output/smooth_position.tif")

for a,b in tqdm(list(combs)):
    #print(str(a) + "|" + str(b))
    run =  str(a) + "_" + str(b) + ".tif"
    segmentedout = "../output/segmented/segmented_" + run
    #segmentedout = "../output/segmented_direct/segmented_" + run

    classifiedout = "../output/classified/class_" + run
    #classifiedout = "../output/classified_direct/class" + run


    #print("segmentation")
    MeanShiftSegmentation(smoothout, segmentedout, spatialr = a, ranger = b)

    segmentImg, segprofile = readRaster(segmentedout)
    ids, stats = segmentStats(segmentImg, RGBImg)
    classified = segmentClustering(stats, 6, segmentImg, ids)
    writeRaster(classifiedout, classified, segprofile)



#######################
#testing classification
#######################

#segmented = "../segmented.tif"
#segmentImg, segprofile = readRaster(segmented)
#RGBImg, RGBprofile = readRaster(inputImg)

#print("calculate stats")
#ids, stats = segmentStats(segmentImg, RGBImg)

#print("main script")

#print("classify")
#classified = segmentClustering(stats, 5, segmentImg, ids)

#print("write raster")
#writeRaster("../classified.tif", classified, segprofile)
