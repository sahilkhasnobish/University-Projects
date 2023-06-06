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
from functions import gym_cost
cost = float(input('Gym membership cost: $'))
friends = int(input('Number of friends signed up: '))
final_cost = gym_cost(cost, friends)
print('\nYour membership cost is ${:.2f}'.format(final_cost))