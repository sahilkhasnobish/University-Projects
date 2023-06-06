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
MONTHS = ['January','February','March','April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']
def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """
    count = 0
    while count!=(m-1):
        count+=1
    name = MONTHS[count]
    return name
def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    for i in range(1,n+1):
        num = randint(low,high)
        values.append(num)
    return values
#values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]
def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    total = 0
    for i in values:
        total+=i
        average = (total/len(values))
    values.sort()
    smallest = values[0]
    largest = values[-1]
#     print(smallest,largest,total,average)
    
    
    return smallest, largest, total, average


