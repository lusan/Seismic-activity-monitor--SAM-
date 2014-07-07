#This script will test the drawing of the world map.
#The idea is to generate a skeleton world map with a code as lucid as possible
#we need to make sure the value of resolution is a Lowercase L,
# for 'low', not a numeral 1
#Code by Lusan Das

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
map = Basemap(projection='ortho', lat_0=50, lon_0=-100,
              resolution='l', area_thresh=1000.0)
 
map.drawcoastlines()
 
plt.show()

#The result was a success. The world map plotted was clear. Different sections of the world map
#can be viewed by changing the lat_0 and lon_0 value.