#This is a mod to PlottingEarthquakeBeta
#Now instead of plotting all of the points at once, we will loop through the points and plot them
#one at a time. When we plot each point, we will adjust the dot size
#according to the magnitude, Since the magnitude start at 1.0, we can simply use
#the magnitude as a scale factor. To get the marker size, we just multiply the
#magnitude by the smallest dot we want on the map.

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

min_marker_size = 2.5
for lon, lat, mag in zip(lons, lats, magnitudes): #zip function takes a number of lists, and pulls  the one item from each list. 
	x, y = map(lons, lats)
	msize = mag * min_marker_size
	map.plot(x,y ,'ro', markersize = 6)

plt.show()

#The result is a success
