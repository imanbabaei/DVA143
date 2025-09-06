"""
Author: Mohd.Reza Babaei
Course: DVA143
Date:   2025-09-04
Lecture 1
Exercise 2
For more info check Lecture1.pdf on canvas -> page 43
"""
# name is string (text) so no need to convert.
name = input('Please enter your name: ')

# age can be integer or float (?!) :| -> convert user input right after calling input() function
# In this example we assume age is an integer
age = int(input('Please enter your age: '))
print('-----')
# it is safe to predefine sleep_time so we don't get any error if none of "if" statements worked. Don't ask how :D
sleep_time = 'Not Found'

if age == 1:
    sleep_time = 14
elif age == 2:
    sleep_time = 13
elif age == 3:
    sleep_time = 12
elif age == 4:
    sleep_time = 11.5
elif 5 <= age <= 6:  # in this case we can also use "or"
    sleep_time = 11
elif age == 7:
    sleep_time = 10.5
elif 8 <= age <= 10:
    sleep_time = 10
elif age == 11:
    sleep_time = 9.5
elif 12 <= age == 15:
    sleep_time = 9
elif age == 16:
    sleep_time = 8.5
elif age >= 17:
    sleep_time = 8

# WARNING!!! In this case we cannot use single quotation to print the string,
# simply -> ' <- in Vårdguiden's close the string variable. You can try this by changing " in print function bellow to '
# pay attention to the colors!
# f for format!
print(f"Hello {name}! According to Vårdguiden's ecommendations, "
      f"individuals your age ({age} years) need to sleep at least {sleep_time} hours per night.")
