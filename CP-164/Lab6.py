"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""
from copy import deepcopy
"""----------- Task 1 ------------"""


def product1(num, n):
    """
    -------------------------------------------------------
    Description:
        Computes the product of num which is: 
            num*num*... repeated n times
        Uses loops
    Assert: num is an integer or float
            n is a positive integer
    Use: result = product1(num,n)
    -------------------------------------------------------
    Parameters:
        num: A number to compute its product (int/float)
        n: Number of times to multiply num (int)
    Returns:
        result: product of num, n times (int/float)        
    -------------------------------------------------------
    """
    assert isinstance(num, int) or isinstance(num, float) and n > 0, 'invalid num or n'
    result = num
    for _ in range(n - 1):
        result *= num
        
    return result


def product2(num, n):
    """
    -------------------------------------------------------
    Description:
        Computes the product of num which is: 
            num*num*... repeated n times
        Uses Recursion
    Assert: num is an integer or float
            n is a positive integer
    Use: result = product1(num,n)
    -------------------------------------------------------
    Parameters:
        num: A number to compute its product (int/float)
        n: Number of times to multiply num (int)
    Returns:
        result: product of num, n times (int/float)        
    -------------------------------------------------------
    """
    assert isinstance(num, int) or isinstance(num, float) and n > 0, 'invalid num or n'
    if n == 0:
        return 1
    return num * product2(num, n - 1)


"""----------- Task 2 ------------"""


def Sn1(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number of the sequence Sn
        S(0) = 1
        S(n) = S(n-1)^2 + 1
        i     :    0    1    2    3    4    
        Sn1(i):    1    2    5    26   677
        Uses Loops
    Assert: i is a non-negative integer
    Use: num = Sn1(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the Sn sequence (int)      
    -------------------------------------------------------
    """
    assert i >= 0, 'invalid i'
    number = 0
    sn = 1
    for _ in range(i):
        sn = ((sn) ** 2) + 1
        
    return sn


def Sn2(i):
    """
    -------------------------------------------------------
    Description:
        Finds the ith number of the sequence Sn
        S(0) = 1
        S(n) = S(n-1)^2 + 1
        i     :    0    1    2    3    4    
        Sn2(i):    1    2    5    26   677
        Uses Recursion
    Assert: i is a non-negative integer
    Use: num = Sn2(i)
    -------------------------------------------------------
    Parameters:
        i: a non-negative number (int)
    Returns:
        number: the ith number in the Sn sequence (int)      
    -------------------------------------------------------
    """
    assert i >= 0, 'invalid i'
    number = i-1
    if i == 0:
        return abs(number) 
    else:
        return (Sn2(i-1)**2)+1
#     Sn2(i) * ((number) ** 2) + 1
    
    
"""----------- Task 3 ------------"""


def countp1(list1):
    """
    -------------------------------------------------------
    Description:
        Counts number of positive numbers in a list
        Uses Loops
    Assert: 'list1' is a non-empty list
            No need to check if items are int/float
    Use: result = countp1(list1)
    -------------------------------------------------------
    Parameters:
        list1: list containing arbitrary numbers (list)
    Returns:
        result: number of positive numbers in list1 (int)        
    -------------------------------------------------------
    """
    assert len(list1) >= 0, 'invalid list1'
    count = 0
    for i in list1:
        if i > 0:
            count += 1
    return count


def countp2(list1):
    """
    -------------------------------------------------------
    Description:
        Counts number of positive numbers in a list
        Uses Recursion
    Assert: 'list1' is of type list
            No need to check if items are int/float
    Use: result = countp2(list1)
    -------------------------------------------------------
    Parameters:
        list1: list containing arbitrary numbers (list)
    Returns:
        result: number of positive numbers in list1 (int)        
    -------------------------------------------------------
    """
    assert len(list1) >= 0, 'invalid list1'
    if list1 == []:
        return 0
    if list1[0] > 0:
        result = 1 + countp2(list1[1:])
    else:
        result = 0 + countp2(list1[1:])
    return result

    
"""----------- Task 4 ------------"""


def get_positives1(list1):
    """
    -------------------------------------------------------
    Description:
        Construct a list of positive numbers in list1
        Uses Loops
    Assert: 'list1' is of type list
            you do not need to assert that list1 items are numbers
    Use: pos_list = get_positives1(input_list):
    -------------------------------------------------------
    Parameters:
        list1: list containing numbers (list)
    Returns:
        pos_list: list containing positive numbers from list1 (list)        
    -------------------------------------------------------
    """
    assert isinstance(list1, list)
    pos_list = []
    for i in list1:
        if i > 0:
            pos_list.append(deepcopy(i))
    return pos_list


def get_positives2(list1):
    """
    -------------------------------------------------------
    Description:
        Construct a list of positive numbers in list1
        Uses Recursion
    Assert: 'list1' is of type list
            you do not need to assert that list1 items are numbers
    Use: pos_list = get_positives2(input_list):
    -------------------------------------------------------
    Parameters:
        list1: list containing numbers (list)
    Returns:
        pos_list: list containing positive numbers from list1 (list)        
    -------------------------------------------------------
    """
    assert isinstance(list1, list)
    if list1 == []:
        return []
    if list1[-1] > 0:
        pos_list = get_positives2(list1[:-1]) + [list1[-1]]
    else:
        pos_list = get_positives2(list1[:-1])
    
    return pos_list
        

"""----------- Task 5 ------------"""


def find_depth1(list1):
    """
    -------------------------------------------------------
    Description:
        Finds the depth of a list
        Assume all list items are of same depth
        Uses loops
    Use: depth = find_depth1(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items of same depth (list)
    Returns:
        depth: an integer reprsenting depth of a list
    -------------------------------------------------------
    """
    depth = 0
    if isinstance(list1, list):
        depth = 1
        while len(list1)>=1 and type(list1[0]) == list: 
            if isinstance(list1[0], list):
                list1 = list1[0]
                depth += 1
                   
    else:
        depth = 0
    return depth


def find_depth2(list1):
    """
    -------------------------------------------------------
    Description:
        Finds the depth of a list
        Assume all list items are of same depth
        Uses Recursion
    Use: depth = find_depth2(list1)
    -------------------------------------------------------
    Parameters:
        list1: a list containing arbitrary items of same depth (list)
    Returns:
        depth: an integer reprsenting depth of a list
    -------------------------------------------------------
    """
    
    depth = 0
    if isinstance(list1,list):
        depth = 1
    if isinstance(list1,list):
        if len(list1)>=1:    
            if not isinstance(list1[0],list):
                return 0
            if list1[0] == []:
                return 1
            else:
                depth = 1+find_depth2(list1[0])
    return depth
