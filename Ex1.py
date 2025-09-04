
n1 = input('Please enter the first number: ')
n2 = input('Please enter the second number: ')
n3 = input('Please enter the third number: ')
print('-----')

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

nf = n1

if n2 > nf:
    nf = n2

if n3 > nf:
    nf = n3

print(f"The largest number entered is {nf}.")
