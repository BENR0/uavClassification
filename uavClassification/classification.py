# -*- coding: utf-8 -*-
import sys
import logging
import numpy as np
import scipy
from skimage.exposure import rescale_intensity
import rasterio as rio
import otbApplication
from sklearn import cluster
# from sys import argv

# TODO
#- add logging and error catching to functions
#- add checks for input image size and proper warnings and/or dependent processing flows
#- add hints for incompatible parameter choices
#- add unit tests with nose
#- put functions in class

# Known Bugs
# - input and output to/from OTB as numpy array does not work in all cases


# logger = logging.getLogger(__name__)


######################
# MEAN SHIFT FILTERING
######################
def MeanShiftSmoothing(inData, outSmooth, outPosition, spatialr = 16, ranger = 16, thres = 0.1, maxiter = 100, innp = False, outnp = False):
    """Wrapper for otbMeanShiftSmoothing application. For more detailed Description of Parameters
    see OTB Cookbook documentation.

    Parameters
    ----------
    inData: string or numpy array
    	Path to input image or if parameter "innp" is True numpy array
    outSmooth: string
      	Path to output image. If parameter "outnp" is True result will be returned as numpy array
    outPosition: string
      	Path to output image for position. If parameter "outnp" is True result will be returned as numpy array
    spatialr: int
   	Spatial radius
    ranger: int
	Range parameter
    thres: float
	Threshold
    maxiter: int
	Maximum number of iterations
    innp: boolean
	If set to True input must be numpy array
    outnp: boolean
	If set to True results will be returned as numpy array

    Return
    ------
    return: numpy array if "outnp" is set to True
    """

    app = otbApplication.Registry.CreateApplication("MeanShiftSmoothing")

    if innp:
        app.SetImageFromNumpyArray("in", inData)
    else:
        app.SetParameterString("in", inData)

    app.SetParameterInt("spatialr", spatialr)
    app.SetParameterFloat("ranger", ranger)
    app.SetParameterFloat("thres", thres)
    app.SetParameterInt("maxiter", maxiter)

    if outnp:
	app.Execute()
	appOutput = app.GetVectorImageAsNumpyArray("fout", "float")
	appPosition = app.GetVectorImageAsNumpyArray("foutpos")
        return appOutput
    else:
	app.SetParameterString("fout", outSmooth)
        app.SetParameterString("foutpos", outPosition)
	app.ExecuteAndWriteOutput()


######################
# MEAN SHIFT SEGMENTATION
######################
def MeanShiftSegmentation(inData, outData, outMode = "raster", segFilter = "meanshift", innp = False, outnp = False):
    """Wrapper for otb Segmentation application. For more detailed Description of Parameters
    see OTB Cookbook documentation.

    Parameters
    ----------
    inData: string or numpy array
    	Path to input image or if parameter "innp" is True numpy array
    outData: string
      	Path to output image. If parameter "outnp" is True result will be returned as numpy array
    outMode: string
	Type of output. Choices are "vector" and "raster"
    segFilter: string
	Type of filter to use for segmentation. Choices are "meanshift", "cc", "watershed", "mprofiles".
    spatialr: int
   	Spatial radius
    ranger: int
	Range parameter
    thres: float
	Threshold
    maxiter: int
	Maximum number of iterations
    innp: boolean
	If set to True input must be numpy array
    outnp: boolean
	If set to True results will be returned as numpy array

    Return
    ------
    return: numpy array if "outnp" is set to True


    TODO
    ----
    - add other parameters documented in OTB cookbook
    """
    app = otbApplication.Registry.CreateApplication("Segmentation")

    if innp:
        app.SetImageFromNumpyArray("in", inData)
    else:
        app.SetParameterString("in", inData)

    app.SetParameterString("mode", outMode)
    app.SetParameterString("filter", segFilter)

    if outMode == "vector":
        app.SetParameterString("mode.vector.out", outData)
	app.ExecuteAndWriteOutput()
    else:
	if outnp:
	    app.Execute()
	    appOutput = app.GetImageAsNumpyArray("mode.raster.out")
	    return appOutput
	else:
	    app.SetParameterString("mode.raster.out", outData)
	    app.ExecuteAndWriteOutput()


######################
# COLOR LABEL SEGMENTATION
######################
def colorMapping(inData, outData, method = "optimal", innp = False, outnp = False):
    """Wrapper for otb colorlabel application. For more detailed Description of Parameters
    see OTB Cookbook documentation.

    Parameters
    ----------
    inData: string or numpy array
    	Path to input image or if parameter "innp" is True numpy array
    outData: string
      	Path to output image. If parameter "outnp" is True result will be returned as numpy array
    method: string
	Method to be used.
	Choices are:
	    - "optimal" calculates optimal look-up table
	    - "custom"
	    - "continuous"
	    - "image"
    innp: boolean
	If set to True input must be numpy array
    outnp: boolean
	If set to True results will be returned as numpy array

    Return
    ------
    return: numpy array if "outnp" is set to True

    TODO
    ----
    - add other parameters documented
    """
    app = otbApplication.Registry.CreateApplication("ColorMapping")

    if innp:
        app.SetImageFromNumpyArray("in", inData)
    else:
        app.SetParameterString("in", inData)

    app.SetParameterString("method", method)

    if outnp:
	app.Execute()
	appOutput = app.GetImageAsNumpyArray("out")
        return appOutput
    else:
	app.SetParameterString("out", outData)
	app.ExecuteAndWriteOutput()


def segmentStats(inSegments, inImg):
    """Calculate statistics for segments

    Parameters
    ----------
    inSegments: numpy array
    	numpy array with dimensions [bands,xdim,ydim] with segments computed for example with MeanShiftSegmentation function
    inImg: numpy array
        Image with spectral data of dimensions [bands,xdim,ydim]

    Return
    ------
    return: list with segment ids, 2D numpy array with stats of each segment per row

    TODO
    ----
    """
    segIds = np.unique(inSegments[0,:,:])
    nbands = inImg.shape[0] - 1 #due to alpha channel
    segStats = np.zeros((len(segIds),6 * nbands))
    segStatsId = []

    numSeg = 0

    for Id in segIds.tolist():
        pixels = inImg[:,inSegments[0,:,:] == Id]
        npixels, tmpnbands = pixels.shape
        # calculate stats for each band
        bandStats = []
        for band in range(nbands):
            tmpstats = scipy.stats.describe(pixels[band,:])
            #stats = list(tmpstats.minmax) + list(tmpstats)[2:]
            stats = list(tmpstats.minmax) + list(tmpstats)[2:]
            if npixels == 1:
                #stats.describe sets variance to NaN
                stats[3] = 0.0
            bandStats += stats

        segStats[numSeg] = bandStats
        segStatsId.append(Id)

        numSeg += 1

    return segStatsId, segStats


def segmentClustering(inData, nclusters, inSegments, segIds):
    """Wrapper for sklearn.cluster.kmeans clustering algorithm

    Parameters
    ----------
    inData: numpy array
    	Data to be clustered. One observation per row
    nclusters: int
        Number of clusters to be generated
    inSegments: numpy array
        segmented image
    segIds: list
        Ids of segments as returned by segmentStats function


    Return
    ------
    return: numpy array
        Classes assigned to each segment of input image

    TODO
    ----
    - add further arguments from sklearn.cluster.kmeans
    """
    kmeans = cluster.KMeans(n_clusters = nclusters)
    kmeans.fit(inData)

    for segId, label in zip(segIds, kmeans.labels_):
        inSegments[0, inSegments[0,:,:] == segId] = label

    return inSegments


def stretchImage(inData):
    """Stretch histogram of array to value range of uint8 using skimage.rescale_intensity

    Parameters
    ----------
    inData: numpy array
        Dimensions [band,xdim,ydim]

    Return
    ------
    return: numpy array

    TODO
    ----
    """
    nbands = inData.shape[0]
    outData = inData.copy()

    for b in range(nbands):
        outData[b,:,:] = rescale_intensity(inData[b,:,:], out_range = (0,255))
        
    return outData


def writeRaster(fName, inData, rioTemplate = None):
    """write numpy array to GTiff raster file with rasterio

    Parameters
    ----------
    fName: string
        Filepath
    inData: numpy array
    	Data to be written
    rioTemplate: rasterio profile dictionary
        Dictionary genereated from rasterio.open().profile

    Return
    ------
    return: 

    TODO
    ----
    - add support for other Formats than GTiff
    - to set profile values when not using template
    """
    nbands, ydim, xdim = inData.shape

    if rioTemplate is not None:
        profile = rioTemplate
        #check dimensions and number of bands of inData compared to template
        if nbands != profile["count"]:
            profile.update(count = nbands)
        if str(inData.dtype) != profile["dtype"]:
            profile.update(dtype = str(inData.dtype))
        if (xdim != rioTemplate["width"]) or (ydim != rioTemplate["height"]):
            sys.exit("The dimensions of the data to be written and the template do not match!\nData was not written.")
    else:
        profile = rio.profiles.DefaultGTiffProfile()
        profile.update(count = nbands, width = xdim, height = ydim )
        


    with rio.open(fName, "w", **profile) as nds:
        for band in range(nbands):
            nds.write(inData[band,:,:].astype(rio.uint8), band + 1)
            

def readRaster(fName, dtype = np.uint8):
    """Read raster file using rasterio

    Parameters
    ----------
    fName: string
        Filepath
    dytpe: numpy dtype. Default np.uint8
        Datatype of the array to which data is read

    Return
    ------
    return: numpy array, rasterio dataset profile

    TODO
    ----
    """
    with rio.open(fName) as ds:
        profile = ds.profile
        outData = ds.read().astype(dtype)

    return outData, profile


    





