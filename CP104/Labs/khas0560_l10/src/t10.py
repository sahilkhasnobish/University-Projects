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
from functions import count_frequency_word
fv = open('words.txt','r')
word = input('Word to count: ')
count = count_frequency_word(fv, word)
print("'{}' appears {} time(s)".format(word,count))