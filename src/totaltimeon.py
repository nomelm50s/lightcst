#!/usr/bin/python3
from lighttime import ontimes 
import os
''' 
totaltimeon gets the total light-ON times for each switch called
Written by: Mike Lemon
Date of Creation: Jan 27, 2022
Version: 0.0.2
'''

# Defines the location of a data file
# TODO: make this a pick list in the gui
csvfile = '~/projects/lightcst/data/LightStatus.csv'

# Accumulate a list of On-times from the data file for the supplied switch name
timelst = (ontimes(csvfile, "Front Lights"))

# Accumulate a list of On-times from the data file for the supplied switch name
timelst = timelst + (ontimes(csvfile, "Back Yard Lights"))

# Writes a list of summarized On-time values to a file
# TODO: Send the output to a table or chart in the gui version
fpath = '/home/mikee/projects/lightcst/data/Lighton.txt'
with open(fpath, 'w') as filehandle:
    for listitem in timelst:
        filehandle.write('%s\n' % listitem)


