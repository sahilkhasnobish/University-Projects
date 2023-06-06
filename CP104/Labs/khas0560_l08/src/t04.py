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
from functions import generate_integer_list
n = int(input('number of values: '))
low = int(input('low value: '))
high = int(input('high value: '))
values = generate_integer_list(n, low, high)
print(values)