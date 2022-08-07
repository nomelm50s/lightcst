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
    f_row = ""  # holds the current row value
    flstart = 0  # Time and date the lights are turned on
    flend = 0  # Time and date the lights are turned off
    on_time = 0  # Temp storage for total on time
    on = 1
    off = 0

    tm_delta = datetime.timedelta()
    tms = []
    #  reads the csv file into a Pandas Data Frame.
    df = pd.read_csv(csvfile)
    #  The date date_format string used to convert to a datetime object
    date_format = '%y/%m/%dT%H:%M:%S]'

    # Find each of the on and off times for each switchname
    # for row in df.iterrows():
    for row in df.itertuples():
        #  if row[3] == switchname:
        if row[3] == switchname:
            # Find the next occurance of on.
            if row[2] == on and p_row == off:
                flstart = datetime.datetime.strptime(row[4], date_format)
            # Find the next occurance of off.
            if row[2] == off and p_row == on:
                flend = datetime.datetime.strptime(row[4], date_format)
                # get the delta of time on
                on_time = flend - flstart
                # Running sum of time on
                tm_delta = tm_delta + on_time
                # convert on_time to a formatted string
                time = str(on_time)
                # convert summary time to a formatted string
                sumtime = str(tm_delta)
                # get a clean datestamp with no time
                datestamp = row[4].split("T")[0]
                # create a list of values
                f_row = [datestamp, switchname, time, sumtime]
                # add a new row to the list
                tms.append(f_row)
                # set the previos row to the current
            p_row = row[2]

    # returns a list of times on
    return tms
