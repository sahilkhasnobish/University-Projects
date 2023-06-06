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
cost = float(input('Enter cost: $'))
quantity = int(input('Enter quantity: '))
total_cost = quantity*cost
print('Given a cost of ${:.2f} and a quantity of {} the total is ${:.2f}'.format(cost,quantity,total_cost))
