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
from functions import pythag
s1 = float(input('Length of side 1: '))
s2 = float(input('Length of side 2: '))
r,d,c,a = pythag(s1, s2)
print('\nRadius of resulting circle: {:.2f}'.format(r))
print('\nDiameter of resulting circle: {:.2f}'.format(d))
print('\nCircumference of resulting circle: {:.2f}'.format(c))
print('\nArea of resulting circle: {:.2f}'.format(a))
