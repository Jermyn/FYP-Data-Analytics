import matplotlib.pyplot as plt
import numpy as np
import csv
import re
import pandas
import sys
import argparse
	

data = pandas.read_csv(sys.argv[-1], sep = ';', na_values='NA')
device_data = data.groupby('Device')
device_data.boxplot(column=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])

# from pandas.tools import plotting
# plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])

# plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])

# plt.figure(figsize=(4, 3))
# data.boxplot(column=['Station1'])

# plt.figure(figsize=(4, 3))
# plt.boxplot(data['FSIQ'] - data['PIQ'])
# plt.xticks((1, ), ('FSIQ - PIQ', ))

plt.show()