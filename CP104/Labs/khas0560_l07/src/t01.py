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
from functions import hi_lo_game
high = int(input('Guess: '))
count = hi_lo_game(high)
print('You made {} guesses.'.format(count))
        
    