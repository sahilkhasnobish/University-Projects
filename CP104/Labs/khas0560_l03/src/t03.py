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
LARGE_DOG_PRICE = 75
SMALL_DOG_PRICE = 50
num_large_dogs = int(input("Number of large dogs groomed: "))
num_small_dogs = int(input("Number of small dogs groomed: "))
total_small_dogs = SMALL_DOG_PRICE*num_small_dogs
total_large_dogs = LARGE_DOG_PRICE*num_large_dogs
total = total_large_dogs+total_small_dogs
print("Total earned for the day: ${:,.2f}".format(total))
