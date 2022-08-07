#!/usr/bin/python3

""" calculate electrical cost class """

from lighttime import ontimes 
from time import time
start = time() # measure run time

class LightCost:
    """ A class that determins electrical cost of night lights """

    def __init__(self, csvfile, logdat, switch_name):
        self.csvfile = csvfile
        self.logdat = logdat
        self.switch_name = switch_name 

    def findtime(self):
        """  determines the lights on time by calling ontimes() """

        return (ontimes(self.csvfile, self.switch_name))

    @classmethod
    def writetime(self):
        """ writes each time period to a file """

        with open(logdat, 'w') as filehandle:
            for listitem in timelst:
                filehandle.write('%s\n' % listitem)
        return 

csvfile = "/home/mikee/projects/01-lightcst/data/LightStatus.csv"
logdat = "/home/mikee/projects/01-lightcst/data/Lighton.txt"

""" calculate the on time for each set of lights """
Flight = LightCost(csvfile, logdat, "Front Lights", )
Blight = LightCost(csvfile, logdat, "Back Yard Lights")

""" create a common log file with all of the on times """    
timelst = Flight.findtime()
timelst = timelst + Blight.findtime()

LightCost.writetime()

# measure run timesudo
end = time()
print(f'It took start {end - start} seconds!')