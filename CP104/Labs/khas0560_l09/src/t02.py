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
from functions import url_categorize
url = input('Enter the website address: ')
url_type = url_categorize(url)
print(url_type)