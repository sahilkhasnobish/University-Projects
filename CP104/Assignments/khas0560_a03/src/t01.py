"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-01-31"
------------------------------------------------------------------------
"""
num_balloons = int(input("Enter number of balloons: "))
num_children = int(input("Enter number of children: "))
ballons_per_child = num_balloons//num_children
ballons_leftover = num_balloons%num_children
print("\nBallons per child: {}\nBalloons left over: {}".format(ballons_per_child,ballons_leftover))