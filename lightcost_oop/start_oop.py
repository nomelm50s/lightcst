# from lighttime import ontimes 
# import os
import pandas as pd
import datetime
from lighttime import ontimes 

class Lightcost:
    ''' '''
    def __init__(self, csvfile, log_file, switch_name):
        self.csvfile = csvfile
        self.log_file = log_file
        self.switch_name = switch_name 

    def Findtime(self):
        return (ontimes(self.csvfile, self.switch_name))

    #print(self.log_file)

    @classmethod
    def Writetime(self):
        with open(self.log_file, 'w') as filehandle:
            for listitem in timelst:
                filehandle.write('%s\n' % listitem)
        return 
    
Lightcost.Writetime()

Flight = Lightcost("Front Lights")
Blight = Lightcost("Back Yard Lights")

timelst = Flight.Findtime()
timelst = timelst + Blight.Findtime()

# print(Flight.switch_name)
# print(Blight.switch_name)

print(timelst)

#qprint(help(Lightcost) )
"~/projects/lightcst/data/LightStatus.csv"
"/home/mikee/projects/lightcst/data/Lighton.txt"