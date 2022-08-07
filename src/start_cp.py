#!/usr/bin/python3
'''
start.py serves as a starting point for the electrical cost calculations. These
calculations only include the outside lights for now.

Written by: Mike Lemon
Date Created: Jan 27, 2022
Version: 0.0.3

 '''
from lighttime_cp import ontimes

# location of the data file created by the Node-RED control program.
# TODO: make this a pick list in the web version.
CSVFILE = '/home/mikee/projects/data/LightStatus.csv'

# creates a list of the Front Lights on-time by day
timelst = (ontimes(CSVFILE, "Front Lights"))

# create a list of Back Yard Lights on-time by day
timelst = timelst + (ontimes(CSVFILE, "Back Yard Lights"))

# Writes the  list of on-time values to the lighton.txt file
# TODO: Send the output to a table or chart in the web version
FPATH = '/home/mikee/projects/data/light_on_001.txt'
with open(FPATH, 'w', encoding="utf8") as filehandle:
    for listitem in timelst:
        filehandle.write(f"{listitem}\n")
