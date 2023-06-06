"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-04-3"
------------------------------------------------------------------------
"""

def customer_by_id(fv, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fv, id_number)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    record = 1
    while record!= '':
        record = fv.readline().rstrip('\n')
        if id_number in record:
            result = record.split(',')
    return result

def customer_first(fv):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    record  = 1
    day_int = 0
    month_int = 12
    result = []
    
    record = fv.readline().strip('\n')
    date = record.split('-')
    while record!='':
        record = fv.readline().strip('\n')
        date = record.split('-')
        if date!=['']:
            first_record = record
            earliest = first_record
             
            month = int(date[-2])
            if month < month_int:
                month_int = month
            day = int(date[-1])
            if day>day_int:
                day_int = day
                if str(month_int) == date[-2] and str(day_int) == date[-1]:
                    result.append(record)
                 
        date = []
    return result

def append_max_num(fv):
    """
    -------------------------------------------------------
    Appends a number to the end of fv. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    first_num = int(fv.readline().strip('\n'))
#     record = num
#     while num!= '':
#         if num > record:
#             record = num
#         num = int(fv.readline().strip('\n'))
#     fv.readline().write("\n{}".format(num))
    num=''
    for i in fv:
        num = int(i.strip())
        if num>first_num:
            first_num = num
        
    fv.readline()
    fv.write("\n{}".format(num))  
    return num
def count_frequency_word(fv, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fv.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fv, word)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        word - the word to search for it in fv (str)
    Returns:
        count - the number of appearance of word in fv (int)
    ------------------------------------------------------
    """
    count = 0
    for i in fv:
        i.strip('\n')
        if word in i:
            count+=1
    return count
def file_copy_n(fv_1, fv_2, n):
    """
    -------------------------------------------------------
    Copies n record from fv_1 (starting from the beginning of the file) to fv2
    Use: file_copy_n(fv_1, fv_2, n)
    -------------------------------------------------------
    Parameters:
        fv_1 - file to search (file - open for reading)
        fv_2 - file to search (file - open for appending)
        n - number of lines to copy from fv_1 to fv_2
    Returns:
        None
    ------------------------------------------------------
    """ 
    count = n    
    for i in fv_1:
        if count!= n:
            fv_2.write(i)
            count+=1 
    return  
        