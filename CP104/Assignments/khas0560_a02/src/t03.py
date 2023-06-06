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
day1_temp_celsius = int(input("Enter temperature for day 1: "))
day2_temp_celsius = int(input("Enter temperature for day 2: "))
day3_temp_celsius = int(input("Enter temperature for day 3: "))
day1_temp_farhenheit = (day1_temp_celsius*(9/5))+32
day2_temp_farhenheit = (day2_temp_celsius*(9/5))+32
day3_temp_farhenheit = (day3_temp_celsius*(9/5))+32
print("\nDay\tC\tF\n1:\t{0}\t{1}\n2:\t{2}\t{3}\n3:\t{4}\t{5}".format(day1_temp_celsius,day1_temp_farhenheit,day2_temp_celsius,day2_temp_farhenheit,day3_temp_celsius,day3_temp_farhenheit))