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


Installation
------------
In order to use the module itself it is sufficient to download all files or clone the repository
and meet the requirements in the "requirements.txt" file.

If the app is to be used it is necessary to install Qt5 as well as PyQt5. The displaying of
results in the app is done with the help of the pyqtgraph module which can be downloaded here
[[http://www.pyqtgraph.org/]]. Untar the archive and place the "pyqtgraph" directory in the same
directory as the app script.

