#1. Functions
#Function that adds up the sum of all even numbers
# def sum():
#     total=0
#     for i in range (0,101,2):
#         total += i
#         if i==100:
#             print(total)

# sum()

#Functions with Parameters
#cannot forward declare functions

#hello(str(5)) cannot forward declare functions

# def hello(name):                #definition
#     print('Hello ' + name)      #name variable exists locally only
#
# hello(str(5))                   #invocation


#Functions with return value and statements
#Using just the return keyword returns none as the value
#
# from random import *
#
# def menu(option):
#     if option == 1:
#         return 'Burger'
#     elif option == 2:
#         return 'Milk'
#     elif option == 3:
#         return 'Tea'
#
#
# r = randint(1, 3)
# choice = menu(r)
#
# print(choice)

#2. Local and Global scope

#local scope cannot use variables in other local scopes
# def spam():
#    eggs = 99
#    bacon()      #Bacon function is called and then local scope is destroyed, moves onto to spam() where eggs=99
#    print(eggs)
#
# def bacon():
#      ham = 101
#      eggs = 0
# spam()

#Global variables can be read from local scope
# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

#Local and Global variables can have the same name


#Global statement
# def spam():
#   global eggs
#   eggs = 'spam' # this is the global
#
# def bacon():
#       eggs = 'bacon' # this is a local
# def ham():
#      print(eggs) # this is the global
#
# eggs = 42 # this is the global
# print(eggs)
# spam()
# print(eggs)

#3. Error Handling (try, except)

# def spam(divideBy):
#     return 42 / divideBy
#
# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error: Invalid argument.')



#############################Guess the Number Game#####################

# from random import *
#
# secretNum = randint(1,20)
# print('Thinking of num from 1 to 20')
# print(str(secretNum));
# for i in range (1,7):
#     print('Take a guess')
#     guess = int(input())
#     if guess < secretNum:
#         print('Too low')
#     elif guess > secretNum:
#         print('Too high')
#     else:
#         break
#
#
# if guess == secretNum:
#     print('You win')
#     print('You guessed it in ' + str(i) + ' num of guesses')
# else:
#     print('You lost, the number was ' + str(secretNum))

# What is a return value? Can a return value be part of an expression?

#############################Collatz Sequence#####################



def collatz(number):
    if number % 2 == 0:
        answer = number // 2
        # print('Inside Func Answer:' + str(answer))
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











