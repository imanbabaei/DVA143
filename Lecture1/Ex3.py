"""
Author: Mohd.Reza Babaei
Course: DVA143
Date:   2025-09-04
Lecture 1
Exercise 3
In this exercise, you will be introduced to generating random numbers with Python.
You should create a script that simulates the dice roll and visualizes the result with
very simple ASCIl art. Start with the following code:

```python
import random
dice = random. randint (1,6)
```python

The function random.randint(1, 6) generates a random integer from 1 to 6 (like a six-sided dice).
The randomized integer is then stored in the variable dice.
Extend the script so that an informative text is printed about the value generated.
Also, visualize the result of the dice roll with ASCII art similar to the examples below:
dice = 2 ->
    print('---------')
    print('| X     |')
    print('|       |')
    print('|     X |')
    print('---------')

dice = 5 ->
    print('---------')
    print('| X   X |')
    print('|   X   |')
    print('| X   X |')
    print('---------')
"""

import random
# Generate a random integer in range [1,6]
dice = random.randint(1, 6)

# let user know what is the dice number.
print(f'You rolled a {dice}!')

if dice == 1:
    print('---------')
    print('|       |')
    print('|   X   |')
    print('|       |')
    print('---------')

if dice == 2:
    print('---------')
    print('| X     |')
    print('|       |')
    print('|     X |')
    print('---------')

if dice == 3:
    print('---------')
    print('| X     |')
    print('|   X   |')
    print('|     X |')
    print('---------')

if dice == 4:
    print('---------')
    print('| X   X |')
    print('|       |')
    print('| X   X |')
    print('---------')

if dice == 5:
    print('---------')
    print('| X   X |')
    print('|   X   |')
    print('| X   X |')
    print('---------')

if dice == 6:
    print('---------')
    print('| X X X |')
    print('|       |')
    print('| X X X |')
    print('---------')
