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
date = int(input('Enter a date in the format YYYYMMDD: '))
year = date//10000
day = date%100
leftover = date//100
month = leftover%100
#year = (date-(date//100000))//10000
print("\n{1:0>2}/{2:0>2}/{0:0>4}".format(year,day,month))