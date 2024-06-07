# Question 1
# There are several valid ways to write this code. Here’s one solution:
import sys

PIN = '0138'
LIMIT = 4

for tries in range(1, LIMIT):
    supplied_pin = input('Enter your PIN: ')
    if supplied_pin == PIN:
        print('Well done, you remembered it!')
        print('... and after only', tries, 'attempts')
        break
# Note the else: is indented with the for loop, not the if!
else:
    print('You had', tries, 'tries and failed!')

# Optional extension to question 1
#
# Using getpass, which is part of the standard library:

import sys
import getpass

PIN = '0138'
LIMIT = 4

for tries in range(1, LIMIT):
    supplied_pin = getpass.getpass('Enter your PIN: ')
    if supplied_pin == PIN:
        print('Well done, you remembered it!')
        print('... and after only' , tries, 'attempts')
        break
# Note the else: is indented with the for loop, not the if!
else:
    print('You had', tries, 'tries and failed!')

#Question 2
var = input("Please enter an integer: ")

if not var.isdecimal():
    print("Invalid integer:", var)
    exit(1)

for var in range(int(var), -1, -2):
    print(var)

#Question 3

y = int(input('Please enter a year: '))

if y % 4 == 0 and (y % 400 == 0 or y % 100 != 0):
    print("Leap Year")
else:
    print("NOT a leap year")



