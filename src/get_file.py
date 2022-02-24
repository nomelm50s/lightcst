#!/usr/bin/python3
""" Creates a numbered list of files found in the target
    directory and prompts for a selection.
    
    File list creator
    Modified to a Python 3 file on Jan 23, 2021
    By: Mike Lemon

"""

from fileinput import filename
import os
import sys

# path to target directory
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

#--------------------------------------------------------------
# sample function for getting file and folder names
# import os

# folder_location = '/home/mikee/projects/'

# def create_file_list(path):
#     return_list = []

#     for filenames in os.walk(path):
#         for file_list in filenames:
#             for file_name in file_list:
#                 if file_name.endswith((".csv")):
#                     return_list.append(file_name)
#     print(return_list)
    
#     return return_list

# file_list = create_file_list(folder_location)
#--------------------------------------------------------------
# Sample method of getting file and folder names
# path = "/home/mikee/projects/"

# for i in os.scandir(path):
#     if i.is_file():
#         print('File: ' + i.path)
#     elif i.is_dir():
#         print('Folder: ' + i.path)