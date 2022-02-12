'''

calclighttime for Python 3
Written by: Mike Lemon
Date of Creation: Jan 25, 2022
Version: 0.0.2

''' 
import datetime
import pandas as pd


def ontimes(csvfile, switchname):

    ''' Calculate the length of time each light is On '''

    
    p_row = 0  # holds the previos row value
    frow = ""  # holds the current row value
    flstart = 0  # Time and date the lights are turned on
    flend = 0  # Time and date the lights are turned off
    ontime = 0  # Temp storage for total ON time
    ON = 1
    OFF = 0
    datetm = datetime.timedelta()
    tms = []

    df = pd.read_csv(csvfile) # reads the csv file into a Pandas Data Frame.
    
    format = '%y/%m/%dT%H:%M:%S]' # The date format string used to convert to a datetime object

    # Find each of the ON time periods for the switchname
    for index, row in df.iterrows():
        if row['Name'] == switchname:
            if row['State'] == ON and p_row == OFF: # Find the first occurance of ON when OFF for the named switch.
                flstart = datetime.datetime.strptime(row['Date'], format)
                
            if row['State'] == OFF and p_row == ON: # Find the first occurance of OFF when ON for the named switch.
                flend = datetime.datetime.strptime(row['Date'], format)

            if flend != 0: # The lights are still ON
                ontime = flend - flstart # delta of ON time
                datetm = datetm + ontime # Running sum of ON times
                time = str(ontime) # convert ontime to a formatted string
                sumtime = str(datetm) # convert summary time to a formatted string
                frow = [switchname, time, sumtime] # store the current values 
                tms.append(frow) # create a list of times 
                flend = 0   # Resets the end point so it's readly for the next loop

            p_row = row['State'] # Done with condition checks, set the previos row to the current.
    
    return(tms) # returns the list of times        

