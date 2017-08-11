import otbApplication
#from rsgislib.segmentation import segutils
from sys import argv

inputImg = "orthofoto_small_cubic_resample.tif"

meanfilter = False
meanseg = False
mapcolor= True
# otbApplication.Registry can tell you what application are available
#print "Available applications : "
#print str( otbApplication.Registry.GetAvailableApplications() )

######################
# MEAN SHIFT FILTERING
######################
outSmooth = "smoothed_img.tif"
outPosition = "position.tif"
if meanfilter:

# The following line creates an instance of the MeanShiftSmoothing application
    MeanShiftSmoothing = otbApplication.Registry.CreateApplication("MeanShiftSmoothing")

# The following lines set all the application parameters:
    MeanShiftSmoothing.SetParameterString("in", inputImg)

    MeanShiftSmoothing.SetParameterString("fout", outSmooth)

    MeanShiftSmoothing.SetParameterString("foutpos", outPosition)

    MeanShiftSmoothing.SetParameterInt("spatialr", 16)

    MeanShiftSmoothing.SetParameterFloat("ranger", 16)

    MeanShiftSmoothing.SetParameterFloat("thres", 0.1)

    MeanShiftSmoothing.SetParameterInt("maxiter", 100)

# The following line execute the application
    MeanShiftSmoothing.ExecuteAndWriteOutput()


######################
# MEAN SHIFT SEGMENTATION
######################
segFilter = "meanshift"
outMode = "raster"
outSeg = "segmentation.tif"

if meanseg:
# Let's create the application with codename "Smoothing"
    app = otbApplication.Registry.CreateApplication("Segmentation")

# We print the keys of all its parameter
#print app.GetParametersKeys()

# First, we set the input image filename
    app.SetParameterString("in", outSmooth)

    app.SetParameterString("mode", outMode)

#app.SetParameterString("mode.vector.out", "SegmentationVector.sqlite")
    if outMode == "vector":
        app.SetParameterString("mode.vector.out", outSeg)
    else:
        app.SetParameterString("mode.raster.out", outSeg)


    app.SetParameterString("filter", segFilter)

# This will execute the application and save the output file
    app.ExecuteAndWriteOutput()



######################
# COLOR LABEL SEGMENTATION
######################
outColorLabel = "colorlabel.tif"
if mapcolor:
# The following line creates an instance of the ColorMapping application
    ColorMapping = otbApplication.Registry.CreateApplication("ColorMapping")

# The following lines set all the application parameters:
    ColorMapping.SetParameterString("in", outSeg)

    ColorMapping.SetParameterString("method","optimal")


    ColorMapping.SetParameterString("out", outColorLabel)

# The following line execute the application
    ColorMapping.ExecuteAndWriteOutput()


