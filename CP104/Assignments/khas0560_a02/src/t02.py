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
p = float(input("Principal: "))
r = float(input("Interest (decimal): "))
t = float(input("Number of years: "))
n = float(input("Compound interest per year: "))
a = p*(1+(r/n))**(n*t)
print("\nBalance: $ {:.2f}".format(a))