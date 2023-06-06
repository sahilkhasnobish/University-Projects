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
from functions import append_max_num
fv = open('numbers.txt', 'w')
num = append_max_num(fv)
print("file 'numbers.txt' open for reading and writing\n{} is appended".format(num))
fv.close()