#Well I know how to zoom, but why not mark a location!
#this program aims to mark Chennai, well this is for you mom

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

#we need to make sure the value of the resolution is a lowercase L,
# for 'low' ,not a numeral 1
# Here the resolution can be changed to h for high, to get better clarity of the map

map = Basemap(projection = 'merc', 
				lat_0 = 13, lon_0 = 80.5, 
					resolution = 'h', area_thresh = 0.1, 
						llcrnrlon = 80, llcrnrlat = 13.2, 
							urcrnrlon = 80.5, urcrnrlat = 13.5)

map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()

lon = 78
lat = 13
x, y = map(lon,lat)
map.plot(x, y, 'bo', markersize = 12)

plt.show()
