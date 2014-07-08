#csv is pretty fun to work with, we just need the latitude and longitude for
#each earthquake.
#This code will attempt at extracting only the latitude and longitude

#Open the earthquake data file
data_file = open('C:\Python27\Py Pro\SAM\dataset.csv')

#Create emmpty lists for the latitudes and longitudes.
lats, lons = [], []

#Read through the entire file, skip the first line,
#and pull out just the lats and lons.
for index, line in enumerate(data_file.readlines()):
	if index > 0:
		lats.append(float(line.split(',')[1]))
		lons.append(float(line.split(',')[2]))
		
#display the first 5 lats and lons
print('lats', lats[0:5])
print('lons', lons[0:5])

#Result is a success
#('lats', [33.8315, 64.3938, 63.5187, 32.817, 38.847332])
#('lons', [-117.5058333, -147.3162, -146.7338, -116.6506667, -122.0111694])
