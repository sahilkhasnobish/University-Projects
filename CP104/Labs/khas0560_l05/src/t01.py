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
from functions import magic_date 
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year (2 digits): "))
magic_date(day, month, year)
if magic_date(day, month, year)==True:
    print('{}/{}/{} is a magic date.')
print(magic_date(day, month, year))

