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
from functions import sum_digit_string
my_str = input('Enter a series of digits: ')
total = sum_digit_string(my_str)
print('The sum is: {}'.format(total))