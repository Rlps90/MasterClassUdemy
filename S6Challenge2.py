#List out  all the odd numbers from 1 to 100 using lists in Python.

numbers = list(range(1, 100))

for x in numbers:
    if x % 2 != 0:
        print(x)