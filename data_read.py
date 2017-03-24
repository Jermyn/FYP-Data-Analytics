#!/usr/bin/env python
import time
import serial
import sys 
import os
from tabulate import tabulate

ser = serial.Serial(
       port= str(sys.argv[1]),#'/dev/tty.usbserial-A402F0YH',#'/dev/tty.usbmodem1411',
       baudrate = int(sys.argv[2]),#115200,
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
count=0
device=[]
deviceBuffer=[]
storageDevice = []

while True:
    for line in ser.read():
    	if line != '\n':
    		if(line=='-'and flag==0):
    			flag=1

    		if((line=='\r'and flag==1) or (line=='a' and flag==1)):
    			flag=2

    		if(flag==1 and line!=' '):
    			rssiStore.append(line)
   
    		if(flag==0 and line!=' '):
    			storage.append(line)
        	# sys.stdout.write(line),
        else:
        	address = ''.join(storage)
        	value = ''.join(rssiStore)
        	storage=[]
        	rssiStore=[]

        	if address in mac:
        		i = mac.index(address)
        		rssi[i] = int(value)
        		storageDevice[i].append(int(value))
        		device[i][1] = value
        		device[i][6] = 0
        	else: 		
        		if(address != ''):
        			mac.append(address)
        			rssi.append(int(value))
        			deviceStorage=[]
        			deviceStorage.append(int(value))
        			storageDevice.append(deviceStorage)
        			deviceBuffer=[]
        			deviceBuffer.append(address)
        			deviceBuffer.append(int(value))
        			deviceBuffer.append(0)
        			deviceBuffer.append(0)
        			deviceBuffer.append(0)
        			deviceBuffer.append(0)
        			deviceBuffer.append(0)
        			device.append(deviceBuffer)

        	z=0
        	while z<len(device):
        		device[z][6]+=1
        		z+=1

        	# recent[:]=[x+1 for x in recent]
        	if(count==30):
        		deviceStorage=[]
        		count=0
        		j = 0
        		while j < len(device):
				   	if device[j][6]>20:
				   		mac.pop(j)
				   		rssi.pop(j)
				   		device.pop(j)
				   		storageDevice.pop(j)
				   	j+=1

        		k=0
        		while k< len(storageDevice):
        			if(len(storageDevice[k])!=0):
	        			m=0
	        			device[k][2]=sum(storageDevice[k])/len(storageDevice[k])
	        			device[k][3]=max(storageDevice[k])
	        			device[k][4]=min(storageDevice[k])
	        			device[k][5]=device[k][3]-device[k][4]
	        			storageDevice[k]=[]
	        		k+=1
        		

       		
        	# print (mac)
        	# print (rssi) 
        	# print(device)
        	# print (recent)
        	# print line
        	# print(storageDevice)
        	os.system('clear')
        	print tabulate(device, headers=["Mac","RSSI","Average", "Max", "Min", "Range", "Last Update"])
        	
        	flag = 0
        	count += 1




