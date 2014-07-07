#This is a mod to the PlotWorldMapBeta.py release. I found a small glitch to the earlier generated world.
#The edges of the world map lacked clarity.
#An attempt has been made to clear the edges, to increase the visibility.


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
map = Basemap(projection = 'ortho', lat_0 = 50, lon_0 = -100, resolution = 'l', area_thresh = 1000.0)
 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()

plt.show()

#The result is a success, the edges are clear now.
