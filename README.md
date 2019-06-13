# Seismic-activity-monitor--SAM-

This app is developed using python to monitor live seismic activity all over the globe.

## How does it work?
It is all about data and how you use them. There are government sites that share datasets which can be parsed and used in accordance to our need. I have used this website http://earthquake.usgs.gov/, to capture data. 
The dataset is in csv format or comma separated value. Now my goal is to parse this data and extract the meaningful information. This information is  used to convert all these datasets to a giant informative map showing live seismic activity all over the globe.

The data set is huge, so the essential fields that I needed was the magnitude, latitude, longitude. The latitude and longitude would help me plot the points and magnitude would help me determine the severity of the earthquake.

## How did I generate the map? 
It is thanks to the Basemap package. Basemap has 24 different mapping projections. Some are global and some can show only a portion of the globe.

When a Basemap class is created, the desired map projection must be specified.

There are two basic ways of doing this. 

One is to provide the latitude and longitude values of each of the four corners of the rectangular map projection region.

The other is to provide the lat/lon value of the center of the map projection region along with the width and height of the region in map projection coordinates

## How did I determine the severity?
The severity has been classified based on the value of the earthquake magnitude. 
If Magnitude < 3
  the plot would be shown by green circle.
else if Magnitude < 5
  The plot would be shown by yellow circle
else
  The plot would be shown by red circle.
  
## What else can be done to make it bigger and better?
We can incorporate neural networks like PyBrain, pyfann with this project, so the app can recognize seismic activity patterns, which can help predict seismic activity, so that we can dream of a safer future.

