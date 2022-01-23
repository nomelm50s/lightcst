from matplotlib import pyplot as plt
import pandas as pd
from datetime import date
from datetime import time
import re, datetime

# df = pd.read_csv('LightStatusc.csv', parse_dates=["Date"])
df = pd.read_csv(csvfile, parse_dates=["Date"])

dts = df["Date"]
sta = df["Time"]
dates =[]

for row in dts:
    match = re.search('\d{2}-\d{2}-\d{2}', row)
    dates.append(datetime.datetime.strptime(match.group(), '%y-%m-%d').date())
    print(dates)
