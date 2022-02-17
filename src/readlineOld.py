#!/usr/bin/python3

import os
import sys
import glob
	
""" Readline old was the first attempt but ultimatly not used. """

def getfname():
	
	""" Prompts for a file name.
	
	Arguments: 
		nothing
	
	Returns:
		the selected file name and path.
		
	Created 11/7/2020 by Mike Lemon
	
	"""

	#dirpath = r"/home/mike/PythonProjects/light_cont/data/"  # the directory that contains the log files
	#prefix = "FileName"
	#fpaths = glob.glob(os.path.join(dirpath, "*.txt".format(prefix)))  # get all the log files
	#testpath = os.path.join(dirpath, "*.txt")
	fpaths = glob.glob("/home/mike/PythonProjects/light_cont/data/*.txt")
	#fpaths.sort(key=lambda fname: int(fname.split('.',1)[0][len(prefix):]))  # sort the log files by number

	print("Log files found:")
	for i,fpath in enumerate(fpaths, 1):
			print("[{}]: {}".format(i, os.path.basename(fpath)))

	choice = int(input("Select a file number to process: "))  # assuming valid inputs
	choice -= 1  # correcting for python's 0-indexing

	print("You have chosen", os.path.basename(fpaths[choice]))
	#items = os.listdir("/home/mike/PythonProjects/light_cont/data/")

	fileName = fpaths[choice]

	#for names in items:
	#	if names.endswith("txt"):
	#		fileList.append(names)

	#cnt = 0
	#for fileName in fileList:
	#	sys.stdout.write( "[%d] %s\n\r" %(cnt, fileName) )
	#	cnt = cnt + 1

	#fileName = int(input("\n\rSelect log file [0 - " + str(cnt - 1) + "]: "))
	#print(fileList[fileName])

	return fileName


def lightstatus(filename):
	
	""" Parses and prints the light switch on times from a file.
	
	Arguments: 
		full path and filename of the target file.
	
	Returns:
		nothing
		
	Created 11/7/2020 by Mike Lemon
	
	"""
	

	count=0
	prevstate = 0
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

