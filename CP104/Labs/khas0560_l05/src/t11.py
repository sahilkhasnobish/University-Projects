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
from functions import quadrant
x = float(input('Enter the x coordinate: '))
y = float(input('Enter the y coordinate: '))
location = quadrant(x, y)
print('\n{}'.format(location))