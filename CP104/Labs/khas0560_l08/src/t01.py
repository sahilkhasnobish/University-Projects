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
from functions import get_weekday_name
d = int(input('Enter day number: '))
name = get_weekday_name(d)
print(name)

DAYS_WEEK = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    count = 0
    while count!=(d-1):
        count+=1
    name = DAYS_WEEK[count]
    return name