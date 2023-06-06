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
from math import pi, sqrt 
NICKEL_VAL = 0.05
DIME_VAL = 0.10
QUARTER_VAL = 0.25
LOONIE_VAL = 1
TOONIE_VAL = 2

FREEZING_POINT = 32

SECONDS_MIN = 60
MINUTES_HOUR = SECONDS_MIN*60
HOURS_DAY = MINUTES_HOUR*24
def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: c = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        c - circumference of a circle (float)
    ------------------------------------------------------
    """
    c = radius*2*pi
    return c 
def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: r, d, c, a = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        r - radius of the resulting circle (float)
        d - diameter of the resulting circle (float)
        c - circumference of the resulting circle (float)
        a - area of the resulting circle (float)
    ------------------------------------------------------
    """
    r = sqrt((s1**2)+(s2**2))
    d = r*2
    c = 2*pi*r
    a = pi*r**2
    return r,d,c,a
def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    cost_nickels = nickels*NICKEL_VAL
    cost_dimes = dimes*DIME_VAL
    cost_quarter = quarters*QUARTER_VAL
    cost_loonies = loonies*LOONIE_VAL
    cost_toonies = toonies*TOONIE_VAL
    total = cost_dimes+cost_loonies+cost_nickels+cost_quarter+cost_toonies
    return total
def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    den = num1*num2
    num = den1*den2
    product = den/num 
    return product,num,den

def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """
    
def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    fahrenheit = (celsius*(9/5))+FREEZING_POINT
    return fahrenheit

def time_values(seconds):
    """
    -------------------------------------------------------
    Returns seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    '''
    days = seconds//ONE_DAY
    hours = seconds//_MINUTES_HOUR
    minutes = seconds//SECONDS_IN_MIN
    return days,hours,minutes
    '''
def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    days = initial_seconds//HOURS_DAY
    hours = initial_seconds%MINUTES_HOUR
    minutes = initial_seconds//SECONDS_MIN
    seconds = initial_seconds%SECONDS_MIN
    return days,hours,minutes,seconds

#(24-(days))%HOURS_DAY
    
    
