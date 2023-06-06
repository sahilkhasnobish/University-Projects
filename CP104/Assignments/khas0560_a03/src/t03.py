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
N = int(input("Enter a positive three digit integer: "))
first_num = N//100
first_two_num = N//10
second_num = first_two_num%10
third_num = N%10
product_num = first_num*second_num*third_num
print("\nThe product of the three digits in the integer ({}) is: {}".format(N, product_num))