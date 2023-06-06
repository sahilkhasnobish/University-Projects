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

sweatband = float(input("Enter Sweatband cost: "))
pants = float(input("Enter pants cost: "))
jacket = float(input("Enter jacket cost: "))
total = float(sweatband + pants + jacket)

print("Clothes      Cost")
print("Sweatband    ${:>6.2f}".format(sweatband))
print("pants        ${:>6.2f}".format(pants))
print("jacket       ${:>6.2f}".format(jacket))
print("total        ${:>6.2f}".format(total))








