import matplotlib.pyplot as plt
import numpy as np
import pandas
import sys
import argparse
import operator
import datetime
import csv
import json
from pprint import pprint

csvfile = open('history_compiled.csv', 'r')
jsonfile = open('history_compiled.json', 'w')
history_write = open('history_compiled.csv', 'w')

# data = pandas.read_csv(sys.argv[-1], sep = ',', na_values='NA')
# device_data = data.groupby('deviceId')
# print device_data

# df = pandas.read_csv('history.csv', delimiter=' ')
# df = df.sort('deviceId')
# print df
# fieldnames = ("time", "deviceId", "mapId", "lat", "lng")
# reader = csv.DictReader(csvfile, fieldnames)
# next(reader)
reader_pre = csv.reader(open("history.csv"), delimiter=",")
sortedlist = sorted(reader_pre, key=operator.itemgetter(1), reverse=False)

for i in sortedlist:
	for num in range(0, 5):
		if num == 4:
			history_write.write(i[num] + "\n")
		else:
			history_write.write(i[num] + ", ")	
# json.dump(sortedlist, history_write, indent = 5, ensure_ascii = False)
jsonfile.write('{"' + 'sample.csv'.replace('.csv', '') + '": [\n')
fieldnames = ("time", "deviceId", "mapId", "lat", "lng")
reader = csv.DictReader(csvfile, fieldnames)
num_lines = sum(1 for line in open('history_compiled.csv')) - 1 
# # next(reader)
# for row in reader:
# 	json.dump(row, jsonfile, sort_keys = True, indent = 5, ensure_ascii = False)
# 	jsonfile.write(",\n")
i = 0
for row in reader:
  i += 1
  json.dump(row, jsonfile, sort_keys = True, indent = 4, ensure_ascii = False)
  if i < num_lines:
    jsonfile.write(',')
  jsonfile.write('\n')
jsonfile.write(']}')


#next(reader)
##Unix conversion of timestamp
#for row in reader:
# 	timestamp = row[0]
# 	value = datetime.datetime.fromtimestamp(int(timestamp))
# 	print(value.strftime('%Y-%m-%d %H:%M:%S'))
#	history_file.write(value.strftime('%Y-%m-%d %H:%M:%S') + "\n")
	

# sortedlist = sorted(reader, key=operator.itemgetter(1), reverse=False)
# json.dump(sortedlist, history_file, indent = 5, ensure_ascii = False)
#history_file.write(sortedlist)

with open('history_compiled.json') as data_file:    
	# for line in data_file:
		data = json.load(data_file)

print (data)    

# data_file.close()

   




#print sortedlist[0]