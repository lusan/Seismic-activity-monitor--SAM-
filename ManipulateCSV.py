#This is a mod to ManipulateData. In ManipulateData parsing was done manually,
#to understand the logic. Python has CSV module, that does it for us.

#This program will produce the same results as earlier, however it does it 
#in a cleaner fashion

import csv

#Open the earthquake data file.
filename = 'C:\Python27\Py Pro\SAM\dataset.csv'

#Create empty lists for the latitudes and longitudes.
lats, lons = [], []

#Read through the entire file, skip the first line,
#and pullout just the lats and lons.
with open(filename) as f:
	#Create a csv reader object
	reader = csv.reader(f)
	
	#Ignore the header row
	next(reader)
	
	#Store the latitudes and longitudes in the appropriate lists.
	for row in reader:
		lats.append(float(row[1]))
		lons.append(float(row[2]))
		
#Display the first 5 lats and lons
print('lats', lats[0:5])
print('lons', lons[0:5])

#Result is a success!!
#('lats', [33.8315, 64.3938, 63.5187, 32.817, 38.847332])
#('lons', [-117.5058333, -147.3162, -146.7338, -116.6506667, -122.0111694])
#The code is more efficient and the with statement statement ensures that the file closes
#properly once it has been read, even if there are errors processing the file. Then we loop through
#each row in the data file, pull out the information we want.