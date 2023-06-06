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
from functions import fraction_product
num1 = int(input('Enter numerator of fraction 1: '))
den1 = int(input('Enter denominator of fraction 1: '))
num2 = int(input('Enter numerator of fraction 2: '))
den2 = int(input('Enter denominator of fraction 2: '))
product,den,num = fraction_product(num1, den1, num2, den2)
print('Product = {}/{}'.format(num,den))
print('Decimal = {}'.format(product))
print(num,den)
