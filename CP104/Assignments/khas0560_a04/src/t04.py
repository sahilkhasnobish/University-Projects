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
from functions import additions
four_num = input('Enter four numbers separated by space: ')
int_num = four_num.split()
a,b,c,d = int_num
number1 = int(a)
number2 = int(b)
number3 = int(c)
number4 = int(d)
first_two, second_two = additions(number1, number2, number3, number4)
print("The sum of the first two numbers {} and the sum of the last two is {}.".format(first_two, second_two))
