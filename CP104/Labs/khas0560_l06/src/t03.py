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
from functions import sum_all
start = int(input('Enter the start: '))
finish = int(input('Enter the finish: '))
increment = int(input('Enter the increment: '))
total = sum_all(start, finish, increment)
print("Total = {}".format(total))

result = 8