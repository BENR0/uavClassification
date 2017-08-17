uavClassification
=================

Script with functions to classify very high resolution orthoimages aquired for example by drone flights.


Module
------
The functions in the module are mostly wrappers for OTB functions as well as reading
and writing raster images with the rasterio package.
Example of a *workflow* using these functions can be found in *script.py* or
*test_smoothing_params.py*


App with Qt Gui
---------------
The script *app_seg_params.py* contains a gui application where an image can be selected
and different segmentation parameters as well as classification parameter can be tested
interactively.

For testing purposes example data can be found in the data directory and is also hard coded
as defaults when no data is selected with the corresponding buttons in the app.

Currently there is no strategy implemented to reduce computation time when big images are
loaded. Thus when changing the sliders for the segmentation parameters there will possibly
be a considerably delay in the display of the result.


Installation
------------
In order to use the module itself it is sufficient to download all files or clone the repository
and meet the requirements in the *requirements.txt* file.

If the app is to be used it is necessary to install Qt5 as well as PyQt5. The displaying of
results in the app is done with the help of the pyqtgraph module which can be downloaded here
[http://www.pyqtgraph.org](http://www.pyqtgraph.org). Untar the archive and place the *pyqtgraph*
directory in the same directory as the app script.


Known Bugs/ Caveats
-------------------
In generall this is a work in progress (also see todos). Unfortunatelly while the wrapper functions
in this module for OTB are in principle designed for it, the input and ouput to the OTB functions as
numpy arrays currently does not work as expected. In consequence some workflows are a little
cumbersome due to the fact that intermediate output hast to be written to disk and subsequently be
read in again for some steps.


Todo
----
In no particular order:

- Create a sampling construction for the app when it is used with larger images in order to minimize
    delay of slider change and display of result
- Add further parameters to wrapper functions (see also the documentation in the functions itself)
- Add functions for estimation of segmentation and classification parameters
- Add further filtering options
- Better handling of big images when using raster output in segmentation
- etc.
