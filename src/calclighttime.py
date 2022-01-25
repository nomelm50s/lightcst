# **********************************************************************************************
# Synopsis: First draft of calclighttime for Python 3
# Written by: Mike Lemon
# Date of Creation: Jan 25, 2022
# Version: 0.0.1
# **********************************************************************************************
import datetime
import pandas as pd

p_row = 0  # holds the previos rows value
frow = ""  # holds front lights time and lable
flstart = 0  # Time the front lights are turned on
flend = 0  # Time the front lights are turned off
blstart = 0 # Time the back lights are turned on
blend = 0  # Time the back lights are turned off
ontime = 0  # Temp storage for a total on time
fronttime = datetime.timedelta()
backtime = datetime.timedelta()

tms = []
i = 1

df = pd.read_csv('/home/mikee/Python_proj/lightcst/data/LightStatus.csv') # reads the csv file into a Pandas Data Frame.

dt = df['Date'] # Get a copy of the Date/Time column as a list of strings

format = '%y/%m/%dT%H:%M:%S]' # The date format string used to convert to a date/time object

dtstart = datetime.datetime.strptime(dt[1], format)

dtend = datetime.datetime.strptime(dt[20], format)

dtdelta = dtend - dtstart

print(dtdelta)

# Find the on time periods for the Front lights
for index, row in df.iterrows():
    if row['Name'] == 'Front Lights':
        if row['State'] == 1 and p_row == 0:
            flstart = datetime.datetime.strptime(row['Date'], format)
            
        if row['State'] == 0 and p_row == 1:
            flend = datetime.datetime.strptime(row['Date'], format)

        if flend != 0:
            ontime = flend - flstart
            fronttime = fronttime + ontime
            print(fronttime)
            frow = ['Front', row['Date'], ontime]
            tms.append(frow)
            flend = 0   # Reset the end point gets it readly for the next loop

        p_row = row['State']

# print(tms)
    
# Find the on time for the Back Lights
for index, row in df.iterrows():
    if row['Name'] == 'Back Yard Lights':
        if row['State'] == 1 and p_row == 0:
            blstart = datetime.datetime.strptime(row['Date'], format)
            
        if row['State'] == 0 and p_row == 1:
            blend = datetime.datetime.strptime(row['Date'], format)
        
        if blend != 0:
            ontime = blend - blstart
            backtime = backtime + ontime
            brow = ['Back', row['Date'], ontime]
            tms.append(brow)
            blend = 0   # Reset the end point to get it ready for the next loop
        
        p_row = row['State']

# print(tms)

