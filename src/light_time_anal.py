from matplotlib import pyplot as plt
import pandas as pd
from datetime import date
from datetime import time
import re, datetime

csvfile = '/home/mikee/Python_proj/lights/lightcst/data/LightStatus.csv'
df = pd.read_csv(csvfile, parse_dates=["Date"])

dts = df["Date"]
# sta = df["Time"]
dates =[]

for row in dts:
    match = re.search('\d{2}-\d{2}-\d{2}', row)
    dates.append(datetime.datetime.strptime(match.group(), '%y-%m-%d').date())
    print(dates)
