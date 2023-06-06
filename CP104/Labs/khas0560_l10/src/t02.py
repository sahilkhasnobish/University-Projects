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
fv = open('customers.txt', 'r')
from functions import customer_by_id
id_number = input('Find customer by id_number\nEnter an ID: ')
print(customer_by_id(fv, id_number))
fv.close()