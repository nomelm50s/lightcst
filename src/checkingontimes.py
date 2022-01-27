from calclighttime import getontimes 


# Define location of data file
csvfile = '/home/mikee/Python_proj/lightcst/data/LightStatus.csv'
# Combine all of the measurements in one list
ontimes = (getontimes(csvfile, "Front Lights"))
ontimes = ontimes + (getontimes(csvfile, "Back Yard Lights"))

print(ontimes)