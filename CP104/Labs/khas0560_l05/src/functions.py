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
ACCELERATION = 9.8
ONE_FRIEND = 0.05
TWO_FRIENDS = 0.10
OVER_THREE = 0.15
def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    if day*month == year:
        magic = True
    else:
        magic = False
        
    return magic
def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg) × acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight = mass*ACCELERATION
    if weight > 1000:
        message = 'heavy'
    elif weight < 10:
        message = 'light'
    else:
        message = 'average'
    return weight, message 
def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """
    if friends == 0:
        final_cost = cost
    elif friends == 1:
        final_cost = cost-(cost*ONE_FRIEND)
    elif friends == 2:
        final_cost = cost-(cost*TWO_FRIENDS)
    else:
        final_cost = cost-(cost*OVER_THREE)
    return final_cost
def closest(target, v1, v2):#COME BACK TO HER 
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    if abs(target-v1)<abs(target-v2):
        result = v1 
    elif abs(target-v1)>abs(target-v2):
        result = v2
    else:
        result = v1
        
    '''
    v2_minus_target = abs(v2-target)#1
    v1_minus_target = abs(v1-target)#-1
    if (target-v2_minus_target)>(target-v1_minus_target):
        result = v1
    elif (target-v2_minus_target)<(target-v1_minus_target):
        result = v2
    else:
        result = v1
    '''
    return result
def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    #year that is exactly divisible by four is a leap
    #year
    #except those divisible by 100
    #except if they are divisible by 400
    if year % 4 == 0 and year%100!= 0:
        result = True 
    elif year%100 == 0 and year%400 == 0:
        result = True 
    else:
        result = False
    return result
def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    if n == 1:
        numeral = 'I'
    elif n==2:
        numeral = 'II'
    elif n==3:
        numeral = 'III'
    elif n==4:
        numeral = 'IV'
    elif n==5:
        numeral = 'V'
    elif n==6:
        numeral = 'VI'
    elif n==7:
        numeral = 'VII'
    elif n==8:
        numeral = 'VIII'
    elif n==9:
        numeral = 'IX'
    elif n==10:
        numeral = 'X'
    else:
        numeral = None
    return numeral 
def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - name of: quadrant, axis, or origin of coordinate x, y (str)
    -------------------------------------------------------
    """
    if x>0 and y>0:
        location = 'Quadrant 1'
    elif x<0 and y>0:
        location = 'Quadrant 2'
    
    elif x<0 and y<0:
        location = 'Quadrant 3'
    elif x>0 and y<0:
        location = 'Quadrant 4'
    elif y==0 and x>0:
        location = 'X-Axis'
    elif x==0 and y>0:
        location = 'Y-Axis'
    else:
        location = 'Origin'
    #x ==0 and y==0
    
    return location 
        
def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time >= 10 years service
        1.5% for full time < 4 years service
        3% for part time > 10 years service
        1% for part time < 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    
    
    
