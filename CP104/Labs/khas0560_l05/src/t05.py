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
from functions import is_leap
year = int(input('Enter a year (>0): '))
result = is_leap(year)
if result == True:
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))