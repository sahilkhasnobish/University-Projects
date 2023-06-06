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
num_flyers = int(input("Number of flyers: "))
num_volunteers = int(input("Number of volunteers: "))
flyers_per_volunteer = num_flyers//num_volunteers
left_over = num_flyers%num_volunteers
print("Flyers per volunteer: {}".format(flyers_per_volunteer))
print("Flyers left over: {}".format(left_over))