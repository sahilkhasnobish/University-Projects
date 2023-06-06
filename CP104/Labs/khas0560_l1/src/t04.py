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
number = int(input('Enter number: '))
percent = float(input('Enter percent: '))
discount = number*(percent/100)
print('A {} percent discount on {} is {:.1f}'.format(percent, number, discount))