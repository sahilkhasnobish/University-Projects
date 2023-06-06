"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-03-26"
------------------------------------------------------------------------
"""
def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    if url.endswith('com'):
        url_type = 'business'
    elif url.endswith('org'):
        url_type = 'non-profit' 
    else:
        url_type = 'other'
    return url_type

def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    product_category = product_code[0:3]
    product_ID = product_code[3:7]
    product_Q = product_code[7:]
    
    if product_category.isupper() and len(product_category) == 3:
        print('Category {} is valid.'.format(product_category))
    else:
        print('Category {} is not valid.'.format(product_category))
    if len(product_ID) == 4:
        print('ID {} is valid.'.format(product_ID))
    else:
        print('ID {} is not valid.'.format(product_ID))
    if product_Q.isupper():
        print('Qualifier {} is valid'.format(product_Q))
    else:
        print('Qualifier {} is not valid'.format(product_Q))
    return 

def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    s_lower = s.lower()

    s_lower_forward = s_lower[0:len(s_lower)]
    s_lower_back = s_lower[::-1]
    if s_lower_forward == s_lower_back:
        palindrome = True 
    else:
        palindrome = False
      
    return palindrome 

def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = ''
    for i in s:
        if i == ',':
            out += '.'
        else:
            out+=i
    return out

def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    d = 0
    s1.lower
    s2.lower
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d+=1
    else:
        d = -1
    return d
    