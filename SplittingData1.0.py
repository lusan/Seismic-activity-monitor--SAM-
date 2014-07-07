#This is a mod to LoadDataset 
#I will try few tweaks in this program which will be helpful when this is used in the project

#Open the earthquake data file
data_file = open('C:\Python27\Py Pro\SAM\dataset.csv')

#Read each line in the file, and keep track of what line we are on.
for index, line in enumerate(data_file.readlines()):
	#Split the data into items in a list.
	split_line = line.split(',')
	
	#Count the number of fields in each line.
	number_fields = len(split_line)
	print(number_fields, split_line)
	
	#Stop after the 5th line of data
	if index == 5:
		break
		
#The result is interesting. We see 15 fields in the header line as expected.
#Python is finding 16 fields in each line of data.
#It must be something to do with the comma in the fields

#well I wont be splitting any files differently, I will be aware of this as I identify
# the index of each , that required from this data.
