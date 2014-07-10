Seismic-activity-monitor--SAM-
==============================

This app is developed using python to monitor live seismic activity all over the globe.

How does it work?
It is all about data and how you use them. There are government sites that share datasets which can be parsed and used in accordance to our need. I have used this website http://earthquake.usgs.gov/, to capture data. 
The dataset is in csv format or comma separated module. Now my goal is to parse this data and extract the meaningful data that I need to convert all these datasets to a giant informative map showing live seismic activity all over the globe.

The data set is huge, so the essential fields that I needed was the magnitude, latitude, longitude. The latitude and longitude would help me plot the points and magnitude would help me determine the seriousness of the earthquake.

How did I generate the map? 
It is thanks to the Basemap package. Basemap has 24 different packages. Some are global and some can show only a portion of the globe.


When a Basemap class is created, the desired map projection must be specified.


There are two basic ways of doing this. 


One is to provide the latitude and longitude values of each of the four corners of the rectangular map projection region.

The other is to provide the lat/lon value of the center of the map projection region along with the width and height of the region in map projection coordinates

I have used Robin projection which is close to a rectangular map.
After successfully generating the map, it was all about manipulating the dataset.

It is an open project. Hence I will be happy if others contribute to this project and make it much bigger.
