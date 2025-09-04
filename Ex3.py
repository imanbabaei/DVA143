import random


dice = random.randint(1, 6)

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
