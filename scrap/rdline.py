#!/usr/bin/python3
""" This module contains functions that create a pick list from 
	a numbered list of files 	and another calculates the time
 	that the outdoor lights are on.

	Date Created: 13 Feb 2022
    
    Created by: Mike Lemon
    
    Version: 0.1    

"""
import os
import sys
import glob

def getfname():
	
	""" creates a numbered list of the data files in a folder and allows one to be selected.
		
	:param None:
	
	:rtype: str
	:return: The file name and full path of the selected file.

	Created 11-9-2020 by Mike Lemon

	TODO: Add a functioin to allow picking the data folder.

	"""

	#Make first pass fail the while test below
	choice = 5000 
	
	#Get the file names and paths
	
	fpaths = glob.glob("../data/*.csv")
	#fpaths = glob.glob("/home/mikee/projects/lightcst/data/*.csv")
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
	
	''' Parses and prints the light switch status from a file 
	to show on and off times for the outside lights.
	
	Arguments: 
		full path and filename of the data file.
	
	Returns:
		nothing
		
	Created 11/7/2020 by Mike Lemon
	
	'''
	prevstate = 0
	
	# print(" ")
	# print(filename)
	
	# Open file for reading each line
	with open(filename, 'r') as file1:
		Lines = file1.readlines() 
		
		for line in Lines: 
			
			# Parse the value of State, skip the first lines
			lightstate = line.split(",")[1] # keep the second element after the comma
			if lightstate != "State" and prevstate != "State": # check that it is past the column lables		

				# Get only the time string from the line
				sampletime = line.split("T")[1] # strip everything to the left f the T
				sampletime = sampletime.split("\"")[0] # strip everything to the right of the Last double quote
			
				sampledate = line.split("T")[0] # Keep everything to the left of the T
				sampledate = sampledate.split("\"")[5] #keep everyting to the right of the last double quote
		
				# print the date, on, and off times
				if int(prevstate) < int(lightstate):
					print("Date:     ", sampledate)
					print("On Time:  ", sampletime)
			
				if int(prevstate) > int(lightstate):
					print("Off Time: ", sampletime)
					print(" ")
			# save thte current lightstate as the previoius	
			prevstate = lightstate

# test line to call the functioins        
lightstatus(getfname())

