#!/usr/bin/python3
"""
The Lightcost class reviews csv log files created by an automated node-RED program.


"""
from lighttime import ontimes 
class Lightcost:
    
    def __init__(self, csvfile, logdat, switch_name):
        self.csvfile = csvfile
        self.logdat = logdat
        self.switch_name = switch_name 

    def Findtime(self):
        ''' converts the string values to times and determines the delta 


        '''
        return (ontimes(self.csvfile, self.switch_name))

    @classmethod
    def Writetime(self):
        with open(logdat, 'w') as filehandle:
            for listitem in timelst:
                filehandle.write('%s\n' % listitem)
        return 
csvfile = "~/projects/lightcst/data/LightStatus.csv"
logdat = "/home/mikee/projects/lightcst/data/Lighton.txt"

Flight = Lightcost(csvfile, logdat, "Front Lights", )
Blight = Lightcost(csvfile, logdat, "Back Yard Lights")
    
timelst = Flight.Findtime()
timelst = timelst + Blight.Findtime()

Lightcost.Writetime()