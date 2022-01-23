import datetime
import pandas as pd

df = pd.read_csv('/home/mikee/Python_proj/lights/lightcst/data/LightStatus.csv') # reads the csv file into a Pandas Data Frame.
dt = df['Date'] # Get a copy of the Date/Time column as a list of strings

format = '%y/%m/%dT%H:%M:%S]' # The date format used to convert to a date/time object

dtstart = datetime.datetime.strptime(dt[1], format)

dtend = datetime.datetime.strptime(dt[20], format)

dtdelta = dtend - dtstart

print(dtdelta)

state = df['State']

for time in state:
    if state[time] == 0:
        ttime 
        print(state)