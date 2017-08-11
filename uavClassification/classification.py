# -*- coding: utf-8 -*-
import logging
import numpy as np
import otbApplication
# from sys import argv

# TODO
#- add logging and error catching to functions
#- add checks for input image size and proper warnings and/or dependent processing flows
#- add hints for incompatible parameter choices
#- add unit tests with nose

##################
# STRUCTURE
#################
#- wrapper functions for otb
#  - smoothing
#  - mean shift segmentation
#- getting values from raster based on segmentation
#- calculate statistics for values
#- k-means classification with scipy

logger = logging.getLogger(__name__)


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
	appOutput = app.GetImageAsNumpyArray("out")
	appPosition = app.GetImageAsNumpyArray("foutpos")
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
outColorLabel = "colorlabel.tif"
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



