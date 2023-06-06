"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Sahil Khasnobish
ID:     190990560
Email:  khas0560@mylaurier.ca
__updated__ = "2020-02-08"
------------------------------------------------------------------------
"""
from random import randint
def calc_federal_tax (income):
    """
    -------------------------------------------------------
    
    Calculates the federal tax. 
    Use: total_fed_tax = calc_federal_tax(income)
    -------------------------------------------------------

    Parameters:
        income: int>0
    Returns
        total_fed_tax: the total federal tax calculated based on the income
        
    -------------------------------------------------------
     """
     
def calc_prov_tax(income):
    """
    -------------------------------------------------------
    
    Calculates the provincial tax. 
    Use: total_prov_tax = calc_prov_tax(income)
    -------------------------------------------------------

    Parameters:
        income: int>0
    Returns
        total_prov_tax: the total provincial tax calculated based on the income
        
    -------------------------------------------------------
     """
    prov_tax = (income-50000) * 0.05
    return(prov_tax)

def num_month(month_int):
    """
    -------------------------------------------------------
    
    Calculates the federal tax. 
    Use: total_fed_tax = calc_federal_tax(income)
    -------------------------------------------------------

    Parameters:
        income: int>0
    Returns
        total_fed_tax: the total federal tax calculated based on the income
        
    -------------------------------------------------------
     """
    if month_int == 1:
        month_str = "January"
    elif month_int == 2:
        month_str = "February"
    elif month_int == 3:
        month_str = "March"
    elif month_int == 4:
        month_str = "April"
    elif month_int == 5:
        month_str = "May"
    elif month_int == 6:
        month_str = "June"
    elif month_int == 7:
        month_str = "July"
    elif month_int == 8:
        month_str = "August"
    elif month_int == 9:
        month_str == "September"
    elif month_int == 10:
        month_str = "October"
    elif month_int == 11:
        month_str = "November"
    elif month_int == 12:
        month_str = "December"
    else:
        month_str = "Invalid month number"
    return month_str
def math_quiz():
    """
    -------------------------------------------------------
    
    Calculates the federal tax. 
    Use: total_fed_tax = calc_federal_tax(income)
    -------------------------------------------------------

    Parameters:
        income: int>0
    Returns
        total_fed_tax: the total federal tax calculated based on the income
        
    -------------------------------------------------------
     """
    first_num = randint(0,999)
    second_num = randint(0,999)
    answer = first_num+second_num
    print("   {:4d}".format(first_num))
    print("+  {:4d}".format(second_num))
    print ()
    student_ans = int(input("Answer: "))
    if student_ans == answer:
        print("Congratulations, correct answer!")
    else:
        print("Incorrect - the answer should be: {}".format(answer))
    return
def additions(number1,number2,number3,number4):
    """
    -------------------------------------------------------
    
    Calculates the federal tax. 
    Use: total_fed_tax = calc_federal_tax(income)
    -------------------------------------------------------

    Parameters:
        income: int>0
    Returns
        total_fed_tax: the total federal tax calculated based on the income
        
    -------------------------------------------------------
     """
    first_two = number1+number2
    second_two = number3+number4
    return first_two, second_two
        