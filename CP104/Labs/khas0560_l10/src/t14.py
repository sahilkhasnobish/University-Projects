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
from functions import file_copy_n
fv_1 = open('words.txt','r')
fv_2 = open('new_words.txt','w')
n = input("Copying 'words.txt' to 'new_words.txt\nNumber of lines to copy: ")
file_copy_n(fv_1, fv_2, n)
fv_1.close()
fv_2.close()
# n = input("Copying 'words.txt' to 'new_words.txt\nNumber of lines to copy: ")
# print(file_copy_n(fv_1, fv_2, n))
# fv_1.close()
# fv_2.close()
