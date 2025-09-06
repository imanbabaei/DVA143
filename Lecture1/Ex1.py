"""
Author: Mohd.Reza Babaei
Course: DVA143
Date:   2025-09-04
Lecture 1
Exercise 1
Create a program where the user enters three numbers. The program should use il statements to identify the input number with the largest numerical value. Then, present the number to the user.
Enter a number: 6
Enter another number: 7
Enter the final number: 2
---
The largest number entered is 7.

Hint: if a >= b and c >= b
      then a >= c
"""

# We repeat input function to get three inputs from user.
n1 = input('Enter a number: ')
n2 = input('Enter another number: ')
n3 = input('Enter the final number: ')
print('-----')

# The output of input function is a string, use int (in this case) to convert n1, n2, and n3 values to integer.
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

# let's assume n1 is the largest number
nf = n1

# if n2 > nf (or n1 :D ) then update nf value with n2
if n2 > nf:
    nf = n2
# if n3 > nf (n1 or maybe n2!) then update nf value with n3
if n3 > nf:
    nf = n3

# print the value of largest number
print(f"The largest number entered is {nf}.")

# In the upcoming weeks you will learn to use list/tuple and max function :)
