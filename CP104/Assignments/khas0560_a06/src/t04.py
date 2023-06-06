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
from functions import print_odds
start = int(input('Enter start value: '))
final = int(input('Enter final value: '))
order = input('Enter order: ')
result = print_odds(start, final, order)
if result == True:
    print('\nReport: Printing completed successfully')
else:
    print('\nReport: Printing Failed')