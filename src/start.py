#!/usr/bin/python3
''' start.py serves as a starting point for the electrical cost calculations. These
calculations only include the outside lights for now.
    
    Written by: Mike Lemon
    Date Created: Jan 27, 2022
    Version: 0.2
    
'''
from lighttime import ontimes 
import os

# location of the data file created by the control program.
# TODO: make this a pick list in the gui
csvfile = '/home/mikee/projects/01-lightcst/data/LightStatus9.csv'

# create a list of on and off times for the Front Lights so the time on can be calculated
timelst = (ontimes(csvfile, "Front Lights"))

# create a list of on and off times for the Back Yard Lights so the time on can be calculated
timelst = timelst + (ontimes(csvfile, "Back Yard Lights"))

# Writes a list of summarized On-time values to a file
# TODO: Send the output to a table or chart in the gui version
fpath = '/home/mikee/projects/01-lightcst/data/Lighton9.txt'
with open(fpath, 'w') as filehandle:
    for listitem in timelst:
        filehandle.write('%s\n' % listitem)



