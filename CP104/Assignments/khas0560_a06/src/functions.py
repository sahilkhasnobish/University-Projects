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

def display_pattern(num_lines):
    """
    -------------------------------------------------------
    
    Calculates the value of growth per year. 
    Use: calc_profit(principal,year)
    -------------------------------------------------------

    Parameters:
        principal: investment amount(float)
        year: number of years(int)
    Returns
        no returns
        
    -------------------------------------------------------
     """
    spaces = 0
    i = 0
    
    if num_lines <= 0:
        print('Invalid number of lines')
    elif num_lines == 1:
        print('#')
    
    else:
        
        print('#')
        while i<(num_lines-2):
            print('#{}#'.format(spaces*' '))
            spaces+=1
            i+=1
        print((num_lines*'#'))
    return
def double_pattern(string1,string2,n):
    """
    -------------------------------------------------------
    
    Calculates the value of growth per year. 
    Use: calc_profit(principal,year)
    -------------------------------------------------------

    Parameters:
        principal: investment amount(float)
        year: number of years(int)
    Returns
        no returns
        
    -------------------------------------------------------
     """
    five = 5
    while n>0:
        for i in range(1,n+1):#try changing the 1 to 0
            if i%2==0 and i<=five:
                print('{} '.format(string2),end='')
            elif i%2==0 and i>five:
                print('\n{} '.format(string2),end='')
                five+=5
            else:
                if i<=five:
                    print('{} '.format(string1),end='')
                elif i==five+1:
                    print('\n{} '.format(string1),end='')
                    five+=5
                else:
                    
                    print('{} '.format(string1),end='')
            
        n-=(n)
    return

def draw_T(width,height,symbol):
    """
    -------------------------------------------------------
    
    Calculates the value of growth per year. 
    Use: calc_profit(principal,year)
    -------------------------------------------------------

    Parameters:
        principal: investment amount(float)
        year: number of years(int)
    Returns
        no returns
        
    -------------------------------------------------------
     """
    spaces = (width-1)//2
    if height < 1:
        print('Error(draw_T): Invalid height')
    elif width%2==0:
        print('Error(draw_T): Invalid width')
    elif width<1:
        print('Error(draw_T): Invalid width')
    else:
        for _ in range(1,width+1):
            print(symbol,end='') 
        print()
        for _ in range(1,height):
            print('{}{}{}'.format(' '*spaces,symbol,' '*spaces))
    return

def print_odds(start,final,order):
    """
    -------------------------------------------------------
    
    Calculates the value of growth per year. 
    Use: calc_profit(principal,year)
    -------------------------------------------------------

    Parameters:
        principal: investment amount(float)
        year: number of years(int)
    Returns
        no returns
        
    -------------------------------------------------------
     """
    five = 0
    if final<=start:
        result = False
    elif (start or final)<-9999 or (start or final)>99999:
        result = False
    else:
        result = True
        while order=='A':
            for i in range(start,final+1):
                          
                if i % 2 != 0:
                    five+=1
                    print('{}     '.format(i),end='')
                    
                
                elif five%5==0:
                    print()
                  
            order = ''
        
        while order == 'D':
            for i in range(final,start-1,-1):
                if i % 2 != 0:
                    print('{}     '.format(i),end='')
                    five+=1
                elif five%5 == 0:
                    print()
            order = ''
                  
    return result
