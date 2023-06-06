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
from functions import factorial
num = int(input('Enter a positive integer: '))
if factorial(num) == -1:
    print('You did not enter a positive integer')
else:
    print('{}! = {}'.format(num,factorial(num)))