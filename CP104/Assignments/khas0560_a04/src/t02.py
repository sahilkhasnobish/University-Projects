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
from functions import num_month
month_int = int(input("Please enter a number between 1 and 12: "))
month_str = num_month(month_int)
print("The month {} is: {}.".format(month_int, month_str))