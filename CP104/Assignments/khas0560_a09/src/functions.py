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

def sum_numbers(text):
    num_list = []
    sum_num = 0
    for i in text:
        text_list = i.split(' ')
        for num in text_list:
            if num.isdigit() and int(num)>0:
                sum_num+=int(num)
                num_list.append(int(num))
       
    return sum_num,num_list

def find_median(scores):
    num_list = []
    
    for line in scores:
        for num in line:
            num.strip('\n')
            if num!='':
                
                num_list.append(num)
                print(num_list)
    return