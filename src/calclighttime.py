# **********************************************************************************************
# Synopsis: First draft of calclighttime for Python 3
# Written by: Mike Lemon
# Date of Creation: Jan 25, 2022
# Version: 0.0.2
# **********************************************************************************************
#
import datetime
import pandas as pd


def getontimes(csvfile, switchname):
    """ This fuction collects the sum of ON times from a CSV file and returns them in a list """
    
    p_row = 0  # holds the previos row values
    frow = ""  # holds the current row values
    flstart = 0  # Time the lights are turned on
    flend = 0  # Time the lights are turned off
    ontime = 0  # Temp storage for total ON time
    ON = 1
    OFF = 0

    datetm = datetime.timedelta()
    tms = []

    df = pd.read_csv(csvfile) # reads the csv file into a Pandas Data Frame.
    
    format = '%y/%m/%dT%H:%M:%S]' # The date format string used to convert to a date/time object

    # Find each of the ON time periods for the named light switch
    for index, row in df.iterrows():
        if row['Name'] == switchname:
            if row['State'] == ON and p_row == OFF: # Find the first occurance of ON when OFF for the named switch.
                flstart = datetime.datetime.strptime(row['Date'], format)
                
            if row['State'] == OFF and p_row == ON: # Find the first occurance of OFF when ON for the named switch.
                flend = datetime.datetime.strptime(row['Date'], format)

            if flend != 0:
                ontime = flend - flstart
                datetm = datetm + ontime
                frow = [switchname, ontime]
                tms.append(frow)
                flend = 0   # Reset the end point gets it readly for the next loop

            p_row = row['State'] # All done set the previos row to the current.
    
    return(tms)        

