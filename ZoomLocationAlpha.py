#This is a alpha code to check zoom in on a region.
#This is an important module to develop as we have many data sets specific
#to one region of the world, which would get lost when plotted on a map of the whole world..
#As I live in chennai, so I will try a zoom in on that region.
#13° N, 82° E
#Bangalore, Coordinates
#llcrnrlon = 77.5, llcrnrlat = 12.9

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

#we need to make sure the value of the resolution is a lowercase L,
# for 'low' ,not a numeral 1
# Here the resolution can be changed to h for high, to get better clarity of the map

map = Basemap(projection = 'merc', 
				lat_0 = 13, lon_0 = 80.5, 
					resolution = 'h', area_thresh = 1000.0, 
						llcrnrlon = 80, llcrnrlat = 13.2, 
							urcrnrlon = 80.5, urcrnrlat = 13.5)

map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()

map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

plt.show()



