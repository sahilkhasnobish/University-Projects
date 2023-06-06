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
from functions import get_weight
mass = float(input("Enter mass (kg): "))
weight,mesage = get_weight(mass)
print('Weight: {} N\n\nObject is: {}'.format(weight,mesage))
