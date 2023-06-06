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
from functions import calc_federal_tax, calc_prov_tax
income = float(input("Total tax liability: $"))
calculated_fed_tax = calc_federal_tax(income)
calculated_prov_tax = calc_prov_tax(income)
print("Federal tax: ${:.0f}\nProvincial tax: ${:.0f}".format(calculated_fed_tax, calculated_prov_tax))