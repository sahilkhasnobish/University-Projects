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
from functions import is_prime
num = int(input('Enter a positive integer: '))
result = is_prime(num)
prime_num = False
while not prime_num:
    if num>1:
        if result == True:
            print('{} is a prime number'.format(num))
        else:
            print('{} is not a prime number'.format(num))
    else:
        num = int(input('Enter a positive integer: '))
    
