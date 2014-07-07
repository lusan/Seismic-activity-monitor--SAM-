#The US government maintains a set of live feeds of earthquake-related data from recent seismic events
#For this project I will use a dataset that contains all seismic events over the last
#seven days, which have a magnitude of 1.0 or greater.

#In my project I will be parsing a file in the csv format also known as
#comma-separated value, after its success I will try json format, but thats a different story :P

#http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.csv
#The above link contains live seismic events over the last seven days, updated every five minutes

data_file = open('C:\Python27\Py Pro\SAM\dataset.csv')

for index, line in enumerate(data_file.readlines()):
	print(line.split(','))
	if index == 1:
		break
		
#Data stored in csv format makes it easier for us to process.
#We process the file by reading each line of the file into our program,
#splitting each line at the commas, and storing the data we care about in the program
#The result is a success