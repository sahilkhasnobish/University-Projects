"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-03-26"
------------------------------------------------------------------------
"""
from functions import is_palindrome
s = input('Enter a string: ')
palindrome = is_palindrome(s)
if palindrome == True:
    print("'{}' is a palindrome".format(s))
else:
    print("'{}' is not a palindrome".format(s))