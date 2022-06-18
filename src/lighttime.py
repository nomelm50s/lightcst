#!/usr/bin/python3

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
     # reads the csv file into a Pandas Data Frame.
    df = pd.read_csv(csvfile)
    # The date date_format string used to convert to a datetime object
    date_format = '%y/%m/%dT%H:%M:%S]'

    # Find each of the ON and OFF times for each switchname
    for row in df.iterrows():
        if row['Name'] == switchname:
            if row['State'] == ON and p_row == OFF: # Find the next occurance of ON.
                flstart = datetime.datetime.strptime(row['Date'], date_format)

            if row['State'] == OFF and p_row == ON: # Find the next occurance of OFF.
                flend = datetime.datetime.strptime(row['Date'], date_format)

                ontime = flend - flstart # get the delta of time ON

                datetm = datetm + ontime # Running sum of time ON

                time = str(ontime) # convert ontime to a formatted string

                sumtime = str(datetm) # convert summary time to a formatted string

                datestamp = row['Date'].split("T")[0] # get a clean datestamp with no time

                frow = [datestamp, switchname, time, sumtime] # create a list of values

                tms.append(frow) # add a new row to the list

            p_row = row['State'] # Done with condition checks, set the previos row to the current

    # returns a list of times ON
    return tms
