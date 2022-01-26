# lightcst

# Automated - Analysis of Electrical Light Use

This project is being created to determine the approximate cost of running the outdoor lights all night. The lights are currently controlled by a node-red flow running on a virtual instance of Ubuntu 20.04. The virtual machine is running on a Windows 10 computer. The Node-RED flow also writes a packet of data to the "LightStatus.csv" CSV file every 2 minutes. The  file is located in the '~/Public/log/' folder and is accessible from any machine on the local network.

A function 'GetRelayState()' in the node-red flow captures the 'date,time', 'device name', and status of each switch on the network.These values are stored in the node-red msg.payload object and then are written to the 'LightStatus.csv' file.

## Functional specifications

* The program needs to read the CSV file and parse the columns into lists.
* The items in the list need to be converted to a date/time object so arithmatic can be used for analysis.
* The date and time need to be converted to date and time data types
* ~~Device names are strings~~
* ~~state should be converted to true or false data type~~
* The approximate current draw needs to be determined for each switch based on the number of bulbs times their documented current draw.
* Once the conversions are complete the total time that the lights are on each day, and the total time on need to be calculated.
* The calculate power use values will be plotted on bar chart versus time.

## Date and Time Conversion

The first part of date and time tracking was getting the date and time stamp into the csv file so it could be easily used in this analysis program later. The date and time is formatted by a Node-RED flow named 'Outside Lights'. The flow manages turning the lights on at night and off in the morning. It also sends a few bits of data from the msg.payload object. The code shown below is the JavaScript code that formats these bits of data and places them in the msg.payload object.

* __name__ contains a unique network name of each switch.

* __state__ is a boolean 1 or 0 that indicates the switch is on or off respectively .

* __ustime__ holds the date and time values in a 24 hour format so the AM and PM flags are not needed.

Finally the values are all stored in payload object and passed along to the write file processes by the return.msg statement.

## GetRelayState Javascript function

``` javascript

name = msg.payload.alias;
state = msg.payload.relay_state;
ustime = new Date().toLocaleString("en-US", {hour12:false, timeZone:"America/Detroit"});

msg.payload = [ustime, name, state];

return msg;

```

[Link to the CalcLightTime notebook](/home/mikee/Python_proj/lightcst/srcCalcLightTime.ipynb)  

This document contains all of the code and comments that was developed to read a csv file as a Pandas date frame. It includes code that illustrates how date and time strings are converted to date and time objects so math operations can be perfomred with them.
