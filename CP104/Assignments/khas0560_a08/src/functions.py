"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-03-27"
------------------------------------------------------------------------
"""
def sum_digit_string(my_str):
    """
    -------------------------------------------------------
    Sums all the digits in my_str, ignores non-digit characters
    Use: total = sum_digit_string (my_str)
    -------------------------------------------------------
    Parameters:
    my_str: string that has single-digit numbers (str)
    returns
    total: sum of all the single digit numbers (integer >= 0)
    -------------------------------------------------------
    """
    num_list = []
    total = 0
    if len(my_str)>0:
        for num in my_str:
            if num.isdigit():
                num_list.append(num)
        for i in num_list:
            number = int(i)
            total+=number
    else:
        total = 'None'
    return total        
def find_frequent(my_str):
    """
    -------------------------------------------------------
    Finds the most frequent character. 
    Use: new_list = find_frequent(my_str)
    -------------------------------------------------------
    Parameters:
    my_str: string(str)
    returns
    new_list: list of frequent characters
    -------------------------------------------------------
    """
    new_list = []
    counter = my_str.count(my_str[0])
    for i in my_str:
        if i.isalpha and i!= ' ':
            if my_str.count(i)>counter and i not in new_list:
                counter = my_str.count(i)
                new_list = [i]
            elif my_str.count(i) == counter and i not in new_list: 
                new_list.append(i)  
    return new_list
def string_capitalizer(my_str):
    """
    -------------------------------------------------------
    Capitalizes in a string. 
    Use: total = sum_digit_string (my_str)
    -------------------------------------------------------
    Parameters:
    my_str: string that has single-digit numbers (str)
    returns
    new_str: new string with capitalized sentences. 
    -------------------------------------------------------
    """
    str_list = []
    new_str = ''
    my_str = my_str.capitalize()
    for i in range(len(my_str)):
        str_list.append(my_str[i])
    for i in range(len(my_str)):
        if str_list[i] == '.' or str_list[i] == '?':
            if i != (len(str_list)-1):
                str_list[i+2] = str_list[i+2].upper()
    for i in range(len(str_list)):
        new_str += str_list[i]
    return new_str

def is_word_chain(my_list):
    """
    -------------------------------------------------------
    Determines if a string is a word chain. 
    Use: result = is_word_chain(my_list) (my_str)
    -------------------------------------------------------
    Parameters:
    my_list: list of strings
    returns
    result: true or false (bool)
    -------------------------------------------------------
    """
    word_list = my_list.split(' ')

    for i in range(len(word_list)-1):

        if (word_list[i][-1]) == (word_list[i+1][0]):
            result = True
        else:
            result = False
     
    return result