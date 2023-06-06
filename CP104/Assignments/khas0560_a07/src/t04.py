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
from functions import keep_positive_numbers, find_value
num_list = keep_positive_numbers()
print('\nList entered: {}'.format(num_list))
target = int(input('\nEnter target = '))
target_list = find_value(num_list, target)
print('\nTarget exists at location(s): {}'.format(target_list))