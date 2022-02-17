#!/usr/bin/python3

# File list creator
# Modified to a Python 3 file on Jan 23, 2021
# By: Mike Lemon
#

from fileinput import filename
import os
import sys

items = os.listdir("/home/mikee/projects/lightcst/data/")

fileList = []

for names in items:
    if names.endswith("csv"):
        fileList.append(names)

cnt = 0
for fileName in fileList:
    sys.stdout.write( "[%d] %s\n\r" %(cnt, fileName) )
    cnt = cnt + 1


fn = int(input("\n\r Select log file [0 - " + str(cnt - 1) + "]: "))

print(fileList[fn])

