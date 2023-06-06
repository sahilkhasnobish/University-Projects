"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""
from copy import deepcopy



def recurrence1(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number in the following recurrence equation:
            S(0) = 10
            S(1) = 25
            S(n) = 3*S(n/2) - 4*S(n-2)
        Note use integer division for S(n/2)
        Uses loops
    Assert: i is a positive integer
    Use: num = recurrence1(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the recurrene equation (int)         
    -------------------------------------------------------
    """
    assert i>0,'i less than 0'
    return

def recurrence2(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number in the following recurrence equation:
            S(0) = 10
            S(1) = 25
            S(n) = 3*S(n/2) - 4*S(n-2)
        Note use integer division for S(n/2)
        Uses Recursion
    Assert: i is a positive integer
    Use: num = recurrence2(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the recurrene equation (int)         
    -------------------------------------------------------
    """
    assert i>0,'i less than 0'
    if i==0:
        return 0
    return (3*recurrence2(i//2))-(4*recurrence2(i-2))

def sum_of_squares1(n):
    """
    -------------------------------------------------------
    Description:
        Finds the sum of squares from 1 to n if n > 0:
            1^2 + 2^2 + 3^2 + ... + n^2
        If n < 0, finds sum of squares from n to -1
            n^2 + ... + -3^2 + -2^2 + -1^2
        For n == 0 returns 0
        Uses loops
    Assert: n is an integer
    Use: total = sum_of_squares1(n)
    -------------------------------------------------------
    Parameters:
        n: an integer referring to upper bound for summation step (int)
    Returns:
        total: sum of squares (int)         
    -------------------------------------------------------
    """
    assert isinstance(n,int),'invalid i'
    total = 0
    if n == 0:
        total = 0
    elif n<0:
        for i in range(n,0): 
            total+=i**2
    else:
        for n in range(n+1):
            total+=n**2
    return total

def sum_of_squares2(n):
    """
    -------------------------------------------------------
    Description:
        Finds the sum of squares from 1 to n if n > 0:
            1^2 + 2^2 + 3^2 + ... + n^2
        If n < 0, finds sum of squares from n to -1
            n^2 + ... + -3^2 + -2^2 + -1^2
        For n == 0 returns 0
        Uses Recursion
    Assert: n is an integer
    Use: total = sum_of_squares2(n)
    -------------------------------------------------------
    Parameters:
        n: an integer referring to upper bound for summation step (int)
    Returns:
        total: sum of squares (int)         
    -------------------------------------------------------
    """
    assert isinstance(n,int),'invalid i'
    if n == 0:
        return 0
    elif n<0:
        return n**2+sum_of_squares2(n+1)
    else:
        return n**2+sum_of_squares2(n-1)

def select_upper1(text,letter):
    """
    -------------------------------------------------------
    Description:
        replace every occurrence of 'letter' in 'text' with upper case
        Function does not change text, returns the updated version of text
        Uses loops
    Assert: text is a string
            letter is a string containing a single lower case alphabet
    Use: modified_text = select_upper1(text,letter)
    -------------------------------------------------------
    Parameters:
        text: a string of arbitrary lenght (str)
        letter: a single lower case character (str)
    Returns:
        modified_text: modified version of the text (str)         
    -------------------------------------------------------
    """
    assert isinstance(text,str)
    modified_text = ''
    for i in text:
        if i == letter:
            modified_text+=i.upper()
        else:
            modified_text+=i
    return modified_text

def select_upper2(text,letter):
    """
    -------------------------------------------------------
    Description:
        replace every occurrence of 'letter' in 'text' with upper case
        Function does not change text, returns the updated version of text
        Uses recursion
    Assert: text is a string
            letter is a string containing a single lower case alphabet
    Use: modified_text = select_upper2(text,letter)
    -------------------------------------------------------
    Parameters:
        text: a string of arbitrary lenght (str)
        letter: a single lower case character (str)
    Returns:
        modified_text: modified version of the text (str)         
    -------------------------------------------------------
    """
    assert isinstance(text,str)
    modified_text = ''
    temp_text = deepcopy(text)
    if len(text)>0:
        if temp_text[0] == letter:
            modified_text+=letter.upper()
            return select_upper2(temp_text[1:], letter)
        
        else:
            modified_text+=temp_text[0]
            return select_upper1(temp_text[1:], letter)
    if len(modified_text) == len(text):
        return ''
  

def is_capitalized1(word):
    """
    -------------------------------------------------------
    Description:
        Checks if given word is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that if the input is a string, then it is a non-empty single-word
        Uses loops
    Assert: word is a string
    Use: result = is_capitalized1(word)
    -------------------------------------------------------
    Parameters:
        word: a non-empty single word (str)
    Returns:
        result: True/False (bool)       
    -------------------------------------------------------
    """
    assert isinstance(word,str),'invalid word'
    if len(word) == 1:
            return word.isupper()
    else:
        if word.isupper():
            for i in range(1,len(word)+1):
                if not (word[i].isupper()):
                    return True
                else:
                    return False
        else:
            return False
#             if word[0].isupper()
#     if len(word) == 1:
#         return word.isupper()
#     else:
#         return word[0].isupper() and word[1:].islower()
    

def is_capitalized2(word):
    """
    -------------------------------------------------------
    Description:
        Checks if given word is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that if the input is a string, then it is a non-empty single-word
        Uses recursion
    Assert: word is a string
    Use: result = is_capitalized2(word)
    -------------------------------------------------------
    Parameters:
        word: a non-empty single word (str)
    Returns:
        result: True/False (bool)       
    -------------------------------------------------------
    """
    assert isinstance(word,str), 'invalid word'
    temp_word = deepcopy(word[1:])
    if len(word) == 1:
        return word.isupper()
    else:
        if word[0].isupper():
            if not temp_word[0].isupper():
                if len(temp_word) == 1:
                    return True 
                else: 
                    return is_capitalized2(temp_word[-1:])
            else:
                return False
        else:
            return False
    
    
def is_title1(text):
    """
    -------------------------------------------------------
    Description:
        Checks if every word in the given text is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that input is always a non-empty string
        Uses loops
    Assert: no asserts
    Use: result = is_title1(word)
    -------------------------------------------------------
    Parameters:
        text: a non-empty string of arbitrary length (str)
    Returns:
        result: True/False (bool)
    -------------------------------------------------------
    """
    result = ''
    count = 0
    word_list = text.split(' ')
    for i in word_list:
        if i.istitle():
            count+=1
    if len(word_list) == count:
        result = True
    else:
        result = False
    return result

def is_title2(text):
    """
    -------------------------------------------------------
    Description:
        Checks if every word in the given text is capitalized
        Capitalized = first letter is upper case and all other letters are lower case
        Assume that input is always a non-empty string
        Uses recursion
    Assert: no asserts
    Use: result = is_title2(word)
    -------------------------------------------------------
    Parameters:
        text: a non-empty string of arbitrary length (str)
    Returns:
        result: True/False (bool)
    -------------------------------------------------------
    """
    
    word_list = text.split(' ')
    if len(word_list) == 1:
        return word_list[0].istitle()

    else:
        if word_list[0].istitle() == True:
            return is_title2(text[text.index(word_list[1]):])
        else:
            return False
    

def binary_flip1(list1):
    """
    -------------------------------------------------------
    Description:
        Pick the first pair of items in a list and swap them
        Repeats the above until the end of list
        If list length is odd, no swaps for the last item
        Function does not change the input list, returns a new list
        Uses loops
    Assert: list1 is a list
    Use: list2 = binary_flip(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items (list)
    Returns:
        list2: updated version of list1 (list)
    -------------------------------------------------------
    """
    assert isinstance(list1,list),'invalid list'
    temp_list = deepcopy(list1)
    list2 = []
    if list1 == []:
        list2 = []
    elif len(list1) == 1:
        list2 = deepcopy(list1)
    else:
        if len(list1)%2 == 0:
            for i in range(len(temp_list)):
                list2.append(deepcopy(i+1))
                list2.append(deepcopy(i))
                temp_list.remove(temp_list[i+1])
                temp_list.remove(temp_list[i])
        else:
            for i in range(len(temp_list)-1):
                list2.append(deepcopy(i+1))
                list2.append(deepcopy(i))
                temp_list.remove(temp_list[i+1])
                temp_list.remove(temp_list[i])
             
    return 
    
def binary_flip2(list1):
    """
    -------------------------------------------------------
    Description:
        Pick the first pair of items in a list and swap them
        Repeats the above until the end of list
        If list length is odd, no swaps for the last item
        Function does not change the input list, returns a new list
        Uses Recursion
    Assert: list1 is a list
    Use: list2 = binary_flip2(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items (list)
    Returns:
        list2: updated version of list1 (list)
    -------------------------------------------------------
    """
    assert isinstance(list1,list),'invalid list'
    temp_list = deepcopy(list1)
    list2 = []
    if temp_list == []:
        return list2
    if len(temp_list) == 1:
        return list2
    else:
        list2.append(deepcopy(temp_list[1]))
        list2.append(deepcopy(temp_list[0]))

        return binary_flip2(temp_list[2:])
        
    
