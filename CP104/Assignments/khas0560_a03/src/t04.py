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
from functions import calorie_calculator
grams_fat = int(input("Enter the fat grams consumed: "))    
grams_carb = int(input("Enter the carbohydrate grams consumed: "))
calories_from_fat, calories_from_carbs = calorie_calculator(grams_fat, grams_carb)
total_cals = calories_from_carbs+calories_from_fat

print('\nTotal Calories: {}'.format(total_cals))
print('Fat Calories: {}'.format(calories_from_fat))
print('Carb Calories: {}'.format(calories_from_carbs))

