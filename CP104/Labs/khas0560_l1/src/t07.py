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
breakfast = float(input('Enter cost of breakfast: $'))
lunch = float(input('Enter cost of lunch: $'))
supper = float(input('Enter cost of supper: $'))
total = breakfast+lunch+supper
#print('{0}\t{1:10>s}\n{2}\t${6:10>.2f}\n{3}\t${7:10>.2f}\n{4}\t${8:10>.2f}\n{5}\t${9:10>.2f}'.format('Meal', 'Cost', 'Breakfast', 'Lunch', 'Supper', 'Total', breakfast,lunch,supper,total))
print('{0:9s}\t{1:9s}\n{2:9s}\t${6:9.2f}\n{3:9s}\t${7:9.2f}\n{4:9s}\t${8:9.2f}\n{5:9s}\t${9:9.2f}'.format('Meal', 'Cost','Breakfast', 'Lunch','Supper', 'Total', breakfast,lunch,supper,total))