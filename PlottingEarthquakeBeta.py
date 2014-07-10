#This is a mod to PlottingEarthquakeAplha
#We will try to make the points on the map represent the magnitude of each earthquake.

import csv

#Open the earthquake data file
filename = 'C:\Python27\Py Pro\SAM\dataset.csv'

#Create empty lists for the data we are interested in
lats, lons = [], []
magnitudes = []

#Read through the entire file, skip the first line,
#and pull out just the lats and lons
with open(filename) as f:
	#Create a csv reader object
	reader = csv.reader(f)
	
	#Ignore the header row
	next(reader)
	
	#Store the latitudes and longitudes in the appropriate lists.
	for row in reader:
		lats.append(float(row[1]))
		lons.append(float(row[2]))
		magnitudes.append(float(row[4]))
		
#-----Build Map----
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection = 'robin', resolution = 'l', area_thresh = 1000.0, lat_0 = 0, lon_0 = -130)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'gray')
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

x, y = map(lons, lats)
map.plot(x,y ,'ro', markersize = 6)

plt.show()

#The result is a success
