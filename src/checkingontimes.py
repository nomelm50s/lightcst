# **********************************************************************************************
# Synopsis: Get all of the light ON times 
#
#
# **********************************************************************************************
from calclighttime import getontimes 


# Define location of a data file
csvfile = './data/LightStatus.csv'

# Combine all of the measurements in one list by calling getontimes for each light
ontimes = (getontimes(csvfile, "Front Lights"))

# calculate the next set of times and concantate them to the list
ontimes = ontimes + (getontimes(csvfile, "Back Yard Lights"))

# Write the values to a file
fpath = './data/Lighton.txt'
with open(fpath, 'w') as filehandle:
    for listitem in ontimes:
        filehandle.write('%s\n' % listitem)
