"""
Author: Mohd.Reza Babaei
Course: DVA143
Date:   2025-09-04
Lecture 1
Exercise 4

Question:
Create a program that asks the user to enter a country.
The program should then respond whether the country is part of the
Nordic region or Great Britain. The comparison should not be case-sensitive.
In other words, it should not matter whether the input is entered in uppercase
or lowercase letters. If the country entered by the user belongs to neither
the Nordic region nor Great Britain, an error message should be displayed.
The Nordic countries include:
• Denmark
• Finland
• Iceland
• Norway
• Sweden
Great Britain includes the countries England, Northern Ireland, Scotland, and Wales.
"""
# Get the user input.
user_input = input('Please enter a name of country: ')

# re-format the text so it will be independent of the user input
standard_name = user_input.capitalize()

# Approach 1: search in list
if standard_name in ['Denmark', 'Sweden', 'Iceland', 'Norway', 'Finland']:
    print(f'{standard_name} is in Nordic Region!')

# Approach 2: if statement
# with "or"/"and" between each condition we can combine multiple if statements
# since the country cannot be in two regions, we use elif (else if) so we might enter each statement only and only once!
if standard_name == 'Sweden' or standard_name == 'Iceland' or standard_name == 'Norway' or standard_name == 'Finland' or standard_name == 'Denmark':
    place = 'Nordic region'
    print(f'{user_input} is in Nordic Region!')
elif standard_name == 'England' or standard_name == 'Wales' or standard_name == 'Northern Ireland' or standard_name == 'Scotland':
    place = 'Great Britain'
    print(f'{user_input} is in Great Britain!')
else:
    # Show the user her/his input :D not the standardized (?!) one.
    print(f'Error 404: {user_input} belongs to neither Nordic region nor Great Britain!')
