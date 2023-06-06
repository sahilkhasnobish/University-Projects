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
from functions import win_game
game_list = win_game()
red_count = game_list[0]
green_count = game_list[1]
print('''\nNumber of "red" entered: {}'''.format(red_count))
print('''Number of "green" entered: {}'''.format(green_count))
if red_count>green_count:
    print('\n"red" team wins!!!')
elif green_count>red_count:
    print('\n"green" team wins!!!')
else:
    print('\ntie')