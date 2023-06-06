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

ASSIGNMENTS = 20
QUIZZES = 10
LAB_TASKS = 10
CLASS_ACTIVITY = 10
MIDTERM = 20
FINAL = 30

assignment_score = float(input("Enter your score in Assignments (0-100): "))
quizzes_score = float(input("Enter your score in Quizzes (0-100): "))
labs_score = float(input("Enter your score in Labs (0-100): "))
classactivities_score = float(input("Enter your score in Class Activities (0-100): "))
Midterm_score = float(input("Enter your score in Midterm (0-100): "))
Final_score = float(input("Enter your score in Final (0-100): "))

weighted_assignments = (assignment_score*ASSIGNMENTS)/100
weighted_quizzes = (QUIZZES*quizzes_score)/100
weighted_labs = (LAB_TASKS*labs_score)/100
weighted_activities = (CLASS_ACTIVITY*classactivities_score)/100
weighted_midterm = (MIDTERM*Midterm_score)/100
weighted_final = (FINAL*Final_score)/100
weighted_score = weighted_assignments+weighted_quizzes+weighted_labs+weighted_activities+weighted_midterm+weighted_final

print('\nWeighted Score in Assignments: {:.0f}'.format(weighted_assignments))
print('Weighted Score in Quizzes: {:.0f}'.format(weighted_quizzes))
print('Weighted Score in Labs: {:.0f}'.format(weighted_labs))
print('Weighted Score in Class Activities: {:.0f}'.format(weighted_activities))
print('Weighted Score in Midterm: {:.0f}'.format(weighted_midterm))
print('Weighted Score in Final: {:.0f}'.format(weighted_final))
print("\nYour weighted score for CP104: {:.0f}".format(weighted_score))

