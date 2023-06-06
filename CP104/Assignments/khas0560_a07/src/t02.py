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
from functions import max_diff
num = input('Enter a list of values: ')
num_list = num.split(',')
a = []
for i in num_list:
    float_num = float(i)
    a.append(float_num) 
md = max_diff(a)
print('\nThe maximum difference is {:.0f}.'.format(md))