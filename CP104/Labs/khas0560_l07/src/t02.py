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
from functions import power_of_two
target = int(input('Enter target number: '))
power = power_of_two(target)
print('The closest power of 2 >= {} is {}.'.format(target,power))