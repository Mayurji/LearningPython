# How to comment in Python

"""
Two ways to comment a line in python

- Using Hash or pound key, # for single comments
- Using triple quotes, ''' for multi-line comments.

"""

# How to print in Python
print('Hello World!')
print("hello again!")
print("this is great")
#print('Im enjoying "this"')
print('Its printing')

# Print using format
money = 10000
print('I have {0} rupees'.format(money))
print('I have {0} rupees and I gave {1}'.format(money, money-1000))

# How to declare variables

car = 10
car_in_use = 6
carInGarage = 4

# Print using f-string
print(f"Car in use {car_in_use}")

# Prompting User for input
cars = input("How many cars do you have: ")

# Taking input from terminal
from sys import argv

# Unpacking arguments from terminal
first, second, third = argv

print(f"first argument: {first}") # first argument is a file name.
print(f"second argument: {second}")
print(f"third argument: {third}")

