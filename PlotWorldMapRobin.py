#This is a minor mod to PlotWorldMapBeta1.3. I will introduce the Robin projection
#of world map, this will give a better visibility of all the countries.


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# we need to make the value of resolution is a lowercase L,
# for 'low', not a numeral 1

map = Basemap(projection = 'robin', lat_0= 0, lon_0 = -100, resolution = 'l', area_thresh = 1000.0)

map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()

map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

plt.show()



