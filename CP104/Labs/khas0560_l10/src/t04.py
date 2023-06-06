"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-04-3"
------------------------------------------------------------------------
"""
fv = open('customers.txt', 'r')
from functions import customer_first
result = customer_first(fv)
print(result)
fv.close()