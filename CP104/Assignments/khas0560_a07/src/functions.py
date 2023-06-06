"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-03-14"
------------------------------------------------------------------------
"""
def win_game():
    """
    -------------------------------------------------------
    Asks the user to enter a series of strings and returns the the number of times red and green appears as a list.
    Use: win_game()
    -------------------------------------------------------
    Parameters:
    none
    Returns:
    game_list(list of integers)
    -------------------------------------------------------
    """
    red_count = 0
    green_count = 0
    game_list = []
    string = input('Enter "red" or "green" or press ENTER to stop: ')
    while string!='':
        new_string = string.lower()
        if new_string == 'red':
            red_count+=1
        elif new_string == 'green':
            green_count+=1
        string = input('Enter "red" or "green" or press ENTER to stop: ')
    game_list.append(red_count)
    game_list.append(green_count)
    return game_list

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
    a - a list of values (list of float)
    Returns:
    md - the largest absolute difference between adjacent values in a (float)
    -------------------------------------------------------
    """
    first_num = a[1]-a[0]
    md = 0
    for i in range(1,len(a)):
        if abs(a[i]-a[i-1])>first_num:
            md = abs(a[i]-a[i-1])
            first_num = md
    return md

def keep_positive_numbers():
    """
    -------------------------------------------------------
    Returns a list with positive integers.
    Use: keep_positive_numbers()
    -------------------------------------------------------
    Parameters:
    none
    Returns:
    positive_list(list with integers)int>1
    -------------------------------------------------------
    """
    n = float(input('Enter a positive integer: '))
    positive_list = []
    while n!=0:
        if n>0 and n.is_integer():
            positive_list.append(int(n))    
        n = float(input('Enter a positive integer: '))
    return positive_list

def find_value(num_list, target):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
    a - a list of values (list of float)
    Returns:
    md - the largest absolute difference between adjacent values in a (float)
    -------------------------------------------------------
    """
    target_list = []
    for i in range(len(num_list)):
        if num_list[i] == target:
            target_list.append(i)
              
               
               
           
    return target_list
