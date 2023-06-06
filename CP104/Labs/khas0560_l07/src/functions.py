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
from random import randint
from math import sqrt
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    
    number = randint(1,high)
    count =  0
    while number!=high:
        if number<high:
            print('Too high, try again.')
        else:
            print('Too low, try again.')
        high = int(input('Guess: '))
        count+=1
    
    print('Congratulations - good guess!')
    return count
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    count = target
    y = ''
    while y!='':
        for i in range(target+1,count+1):
            if sqrt(target).is_integer():
                power = target**2
            elif (sqrt(i)).is_integer():
                power = target**2
                count+=1
        target = int(input('Enter target number: '))
        
    return power
            
        #if the sqrt of the nearest number .is_integer
    #then it is a nearest power of two
    