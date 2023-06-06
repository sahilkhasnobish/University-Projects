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
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
print('The date: {2:0>4d}/{1:0>2d}/{0:0>2d}'.format(day,month,year))
