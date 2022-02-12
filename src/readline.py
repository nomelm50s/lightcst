import os
import sys
import glob

def getfname():
	
	''' List all log files in the data folder as menu items and allows selection by number.

	Arguments:
		None
	
	Returns:
		The full file name and path to the selected file.

	Created 11-9-2020 by Mike Lemon

	'''
	#Make first pass fail the while test below
	choice = 5000 
	
	#Get the file names and paths
	fpaths = glob.glob("/home/mike/PythonProjects/light_cont/data/*.txt")
	
	#Print a list of the files found
	print("Files found:")
	for i,fpath in enumerate(fpaths, 1):
			print("[{}]: {}".format(i, os.path.basename(fpath)))

	maxchoice = len(fpaths)

	#Get user selection until a valid number is selected
	while (choice > len(fpaths)):
		choice = int(input("Select a file number to process: "))  # assuming valid inputs
	
	else:
		
		choice -= 1  # correcting for python's 0-indexing
		if choice < 0:
			choice = 0
		print(" ")
		print("You have chosen", os.path.basename(fpaths[choice]))

	fileName = fpaths[choice]

	return fileName


def lightstatus(filename):
	
	''' Parses and prints the light switch status from a file created 
	on the Pi3 to show on and off times for the outside lights.
	
	Arguments: 
		full path and filename of the target file.
	
	Returns:
		nothing
		
	Created 11/7/2020 by Mike Lemon
	
	'''
	count=0
	prevstate = 0
	print(" ")
	print(filename)
	
	# Open file for reading each line
	file1 = open(filename, 'r') 
	Lines = file1.readlines() 
	
	# Iterate through each line
	for line in Lines: 
		
		lightstate = line.split(":")[6]
		lightstate = lightstate.split("}")[0]
		
		sampletime = line.split("T")[1]
		sampletime = sampletime.split("-")[0]
		
		sampledate = line.split("\"")[3]
		sampledate = sampledate.split("T")[0]

		if int(prevstate) < int(lightstate):
			print("Date:   ", sampledate)
			print("On Time:  ", sampletime)
		
		if int(prevstate) > int(lightstate):
			print("Off Time: ", sampletime)
			print(" ")
			
		prevstate = lightstate
	
	# Close file when done
	file1.close()
        
lightstatus(getfname())

