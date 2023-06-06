"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-02-28"
------------------------------------------------------------------------
"""
from math import sqrt

GROWTH = 0.05
def calc_profit(principal,year):
    """
    -------------------------------------------------------
    
    Calculates the value of growth per year. 
    Use: calc_profit(principal,year)
    -------------------------------------------------------

    Parameters:
        principal: investment amount(float)
        year: number of years(int)
    Returns
        no returns
        
    -------------------------------------------------------
     """
    print('Year\tValue (Million Dollars)')
    print('---- -----------------------')
    for i in range(1,year+1):
        growth_year = (principal*GROWTH)+principal
        principal = growth_year
        print('   {}                {:1>.6f}'.format(i,principal))
    return

def perfect_square(num):
    """
    -------------------------------------------------------
    
    Calculates all the perfect squares.. 
    Use: perfect_square(num)
    -------------------------------------------------------

    Parameters:
        num (int>0)
    Returns
        no returns
        
    -------------------------------------------------------
     """
    if num<0:
        print('\nYou did not enter a positive integer')
    else:
        print('\nPerfect squares below {} are: '.format(num),end='')
        for i in range(1,num):
            if i%(sqrt(i)) == 0:
                print('{}'.format(i),end=', ')
        
        
    return 



def factorial(num):
    """
    -------------------------------------------------------
    
    Calculates the factorial numbers. 
    Use: factorial(num)
    -------------------------------------------------------

    Parameters:
        num: int>0
    Returns
        result: the factorials
        
    -------------------------------------------------------
     """
    factorial_num = 1
    if num > 0:
        for i in range(1,num+1):
            factorial_num *=i
            if i == num:
                result  = factorial_num
    else:
        result = -1
    return result

def is_prime(num):
    """
    -------------------------------------------------------
    
    Determines if a number is a prime number. 
    Use: is_prime(num)
    -------------------------------------------------------

    Parameters:
        num: int>0
    Returns
        result: True or False
        
    -------------------------------------------------------
     """
    result = True
    if num>1:
        for i in range(2,num,1):
            if num%i==0:
                result = False
    return result



        
        