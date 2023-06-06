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
from functions import closest
target = float(input('Enter target: '))
v1 = float(input('Enter v1: '))
v2 = float(input('Enter v2: '))
result = closest(target, v1, v2)
print('Closest value to {} is {}'.format(target,result))