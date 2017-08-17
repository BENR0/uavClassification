uavClassification
=================

Script with functions to classify very high resolution orthoimages aquired for example by drone flights.


App with Qt Gui
---------------

The script app_seg_params.py contains a gui application where an image can be selected
and different segmentation parameters as well as classification parameter can be tested
interactively.

For testing purposes example data can be found in the data directory and is also hard coded
as defaults when no data is selected with the corresponding buttons in the app.

Currently there is no strategy implemented to reduce computation time when big images are
loaded. Thus when changing the sliders for the segmentation parameters there will possibly
be a considerably delay in the display of the result.

