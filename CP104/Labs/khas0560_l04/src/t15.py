"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2019-09-20"
------------------------------------------------------------------------
"""
'''
from functions import time_split
initial_seconds = int(input('Number of seconds: '))
days,hours,minutes,seconds = time_split(initial_seconds)
print(days,hours,minutes,seconds)
'''
import functions 

initial_seconds = int(input('Number of seconds: '))
days,hours,minutes=functions.time_split(initial_seconds)
print('The days,hour and min are: {}{}{}'.format(days,hours,minutes))

