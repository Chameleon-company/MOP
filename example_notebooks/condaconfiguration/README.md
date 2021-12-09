<img src="/images/mop-black.png" alt="drawing" width="100"/>

# Melbourne Open Data Playground
## SETTING UP A CONDA ENVIRONMENT IN ANACONDA

Last Updated: 10-Nov-2021

### Installing the environment
#### Pre-requisites
- Anaconda installed on Windows Environment
- [Copy this conda environment configuration file](environment.yml) to a local directory

#### Installation steps
To setup a new environment with Conda follow these steps:

1) Launch Anaconda

2) Goto to the "base" environment

3) Launch Command Prompt

4) Run the following commands:

&emsp;&gt;cd {directory containing the environment.yml file}

&emsp;&gt;conda env create -f environment.yml

5) In Anaconda install JupyterNotebook


### Removing thee environment
To remove the environment repeat steps 1 through 3 above then run the following command

&gt;conda env remove -n MelbourneCityOpenData

### Environment Packages
The following packages make up the MelbourneCityOpenData environment.

#### CORE
**requests**&emsp;&emsp;HTTP Library<br>

#### DATA ENGINEERING
**numpy**&emsp;&emsp;Array computation<br>
**pandas**&emsp;&emsp;Data structures for data analysis, time series, and statistics<br>

#### DATA SCIENCE/ML
**scikit-learn**&emsp;&emsp;Machine/Statitical learning<br>

#### VISUALISATION AND IMAGE PROCESSING
**matplotlib**&emsp;&emsp;Plotting Library for static, animated, and interactive visualizations<br>
**seaborn**&emsp;&emsp;Extends MatPlotlib with more sophisticated plot types<br>
**plotly**&emsp;&emsp;Create interactive graphs in Jupyter notebook<br>

#### OPEN DATA
**sodapy**&emsp;&emsp;python interface to SOCRATA API<br>

#### GEOSPATIAL
**pyproj**&emsp;&emsp;interface to PROJ (cartographic projections and coordinate transformations library)<br>
**shapely**&emsp;&emsp;Manipulation and analysis of geometric objects in the Cartesian plane.<br>
**geopandas**&emsp;&emsp;Extends the datatypes used by Pandas to allow spatial operations on geometric types.<br>
&emsp;&emsp;&emsp;Geometric operations are performed by shapely.<br>
&emsp;&emsp;&emsp;Geopandas further depends on fiona for file access and matplotlib for plotting.<br>
**geopy**&emsp;&emsp;Python client for several popular geocoding web services.<br>
&emsp;&emsp;&emsp;geopy includes geocoder classes for the OpenStreetMap Nominatim, Google Geocoding API (V3), and many other geocoding services.
**folium**&emsp;&emsp;makes it easy to visualize data that’s been manipulated in Python on an interactive leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing rich vector/raster/HTML visualizations as markers on the map.<br>
&emsp;&emsp;&emsp;The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. folium supports both Image, Video, GeoJSON and TopoJSON overlays.<br>