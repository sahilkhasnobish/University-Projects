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
from functions import sum_numbers
text = open('text_numbers.txt','r')
sum_num, num_list = sum_numbers(text)
print(sum_num, num_list)
