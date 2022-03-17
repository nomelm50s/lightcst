#!/usr/bin/python3

""" calculate electrical cost class """

from lighttime import ontimes 
from time import time
start = time()

class Lightcost:
    
    """ A class that determins electrical cost of night lights """

    def __init__(self, csvfile, logdat, switch_name):
        self.csvfile = csvfile
        self.logdat = logdat
        self.switch_name = switch_name 

    def Findtime(self):
    
        """  determines the lights on time by calling ontimes() """

        return (ontimes(self.csvfile, self.switch_name))

    @classmethod
    def Writetime(self):
        
        """ writes each time period to a file """

        with open(logdat, 'w') as filehandle:
            for listitem in timelst:
                filehandle.write('%s\n' % listitem)
        return 

csvfile = "/home/mikee/projects/lightcst/data/LightStatus.csv"
logdat = "/home/mikee/projects/lightcst/data/Lighton.txt"

""" calculate time on for each set of lights """
Flight = Lightcost(csvfile, logdat, "Front Lights", )
Blight = Lightcost(csvfile, logdat, "Back Yard Lights")

""" create a common log file of the on time values """    
timelst = Flight.Findtime()
timelst = timelst + Blight.Findtime()

Lightcost.Writetime()

end = time()
print(f'It took {end - start} seconds!')