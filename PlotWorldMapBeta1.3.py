#This is a mod to the PlotWorldMapBeta1.2. An attempt to draw the latitude and 
#longitude lines has been made. 

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# we need to make the value of resolution is Lowercase L;
#for 'Low' not a numeral 1

map = Basemap(projection = 'ortho', lat_0 = 50, lon_0 = -100, resolution = 'l', area_thresh = 1000.0)

map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()

#np.arange () tells arguments where the latitude and longitude should begin and end

map.drawmeridians(np.arange(0, 360, 30))  
map.drawparallels(np.arange(-90, 90, 30))

plt.show()

#The result is a success, the latitude and longitude lines are clear and distinct.
#If the latitude and longitude parameteres in the original definition are set to  0 and 
#-100 respectively, the result would be the map centered along the equator, it has been 
#tested and it works fine under different parameters.
