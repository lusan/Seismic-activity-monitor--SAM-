#After all the mods, its time for the final release version
#This powerful code is capable parsing a giant text and converting it to an
#informative map representing seismic activity all over the globe!
import csv

#Open the earthquake data file
filename = 'C:\Python27\Py Pro\SAM\dataset.csv'

#Create empty lists for the data we are interested in
lats, lons = [], []
magnitudes = []
timestrings = []

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
		timestrings.append(row[0])
		
#-----Build Map----
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

def get_marker_color(magnitude):
	#Returns green for small earthquakes, yellow for moderate earthquakes
	#red for significant earthquakes
	if magnitude < 3.0:
		return ('go')
	elif magnitude < 5.0:
		return ('yo')
	else:
		return ('ro')

map = Basemap(projection = 'robin', resolution = 'l', area_thresh = 1000.0, lat_0 = 0, lon_0 = -130)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'gray')
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

min_marker_size = 2.25
for lon, lat, mag in zip(lons, lats, magnitudes): #zip function takes a number of lists, and pulls  the one item from each list. 
	x, y = map(lons, lats)
	msize = mag * min_marker_size
	marker_string = get_marker_color(mag)
	map.plot(x,y ,marker_string, markersize = msize)

title_string = "Earthquake of Magnitude 1.0 or greater \n"
title_string += "%s through %s" % (timestrings[-1][:10], timestrings[0][:10])	
plt.title(title_string)


plt.show()

#The result is a success
