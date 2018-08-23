"""
--------------------------------------------------------
1. Functions
a. Return value
b. Parameters or arguments
--------------------------------------------------------
"""
# Example 1: Pre-defined APIs or library methods that Python provides us
print('1. Print(), input(), len(), range(), randint(), etc')
print('Hello World\nName?')
myName= input()
print('Good to meet you ' + myName)
print(len(myName))

# Print method additional functionalities that Python provides -> (end and sep)
# 1. To have continuous 2 print statements separated with some special character like space, comma, etc
print('hello ', end='')
print('cats')
print('hello world', end='.')
print('\n')
# 2. Special character separated
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')

print('\n2. Custom methods - Function that adds up the sum of all even numbers')
# functionName = sum
# return type = int
# arguments/parameters = no args
def sum():
    total=0
    for i in range (0,101,2):
        total += i
        if i==100:
            print(total)

sum()

print('\n3. Custom methods - Function that adds up the sum of all even numbers')

# functionName = sayHello
# return type = none
# arguments/parameters = string
def sayHello(name):                # function definition
    print('Hello ' + name)      # name variable exists locally only

sayHello(str(5))                   # function invocation


print('\n4. Custom methods - Function that returns a random menu option')
from random import *

def menu(option):
    if option == 1:
        return 'Burger'
    elif option == 2:
        return 'Milk'
    elif option == 3:
        return 'Tea'

r = randint(1, 3)
choice = menu(r)
print(choice)

print('\n4. Custom methods - Function that asks user to guess a number it is thinking')
from random import *

secretNum = randint(1,20)
print('Thinking of num from 1 to 20')
print('Shhh its ' + str(secretNum));
for i in range (1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNum:
        print('Too low')
    elif guess > secretNum:
        print('Too high')
    else:
        break

if guess == secretNum:
    print('You win')
    print('You guessed it in ' + str(i) + ' num of guesses')
else:
    print('You lost, the number was ' + str(secretNum))


print('\n5. Custom methods - Function that prints Collatz sequence')
def collatz(number):
    if number % 2 == 0:
        answer = number // 2
        print('Inside Func Answer:' + str(answer))
        return answer
    elif number % 2 == 1:
        answer = 3 * number + 1
        return answer

print('Enter a number:')
try:
    finalAns = int(input())
except ValueError:
    print('Error: Invalid integer.')

while finalAns != 1:
    finalAns = collatz(finalAns)
    print('Final Answer:' + str(finalAns))
