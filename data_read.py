#!/usr/bin/env python
import time
import serial
import sys 
import os
from tabulate import tabulate

ser = serial.Serial(
       port='/dev/tty.usbmodem1421',
       baudrate = 9600,
       parity=serial.PARITY_NONE,
       stopbits=serial.STOPBITS_ONE,
       bytesize=serial.EIGHTBITS,
       timeout=1
       )

flag =0
mac=[]
rssi=[]
storage=[]
rssiStore=[]
recent=[]
count=0
device=[]
deviceBuffer=[]

while True:
    for line in ser.read():
    	if line != '\n':
    		if(line==']'):
    			flag=0;

    		if(flag==2 and line!=' '):
    			if(line =='\r'):
    				flag=0;
    			else:
    				rssiStore.append(line)

    		if(flag==1 and line!=' '):
    			storage.append(line)

    		if(line=='['):
    			flag=1;
    		if(line=='i'):
    			flag=2;

        	# sys.stdout.write(line),
        else:
        	address = ''.join(storage)
        	value = ''.join(rssiStore)
        	storage=[]
        	rssiStore=[]

        	if address in mac:
        		i = mac.index(address)
        		rssi[i] = value
        		recent[i] = 0
        		device[i][1] = value
        	else:
        		if(address != ''):
        			mac.append(address)
        			rssi.append(value)
        			recent.append(0)
        			deviceBuffer=[]
        			deviceBuffer.append(address)
        			deviceBuffer.append(value)
        			device.append(deviceBuffer)


        	recent[:]=[x+1 for x in recent]
        	if(count==30):
        		count=0
        		j = 0
        		while j < len(recent):
				   if recent[j] > 20:
				    	mac.pop(j)
	        			rssi.pop(j)
	        			recent.pop(j)
	        			device.pop(j)
				   else:
       					j += 1

       		
        	# print (mac)
        	# print (rssi) 
        	# print(device)
        	# print (recent)
        	# print line
        	os.system('clear')
        	print tabulate(device)
        	
        	flag = 0
        	count += 1




