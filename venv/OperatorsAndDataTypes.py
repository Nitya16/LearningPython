#1.Operators follow BO(Exponent)ModulusDMAS
# 1- **
# 2- * / //(Integer Division 22//8 = 6) %
# 3- - +
#Note: = is assignment operator (puts value on right to left)
#2.Data Types & Operators

# int, float, str , none, list
#
# spam = print('hi')
# print(None == spam)         #True


#2.1Using methods: print(), input(), len()


# print('Hello World')
# print('Name?')
# myName= input()
# print('Good to meet you ' + myName)
# inputL= len(myName)       #input() function returns a string
# print(inputL)

#Print method functions-> (end and sep)

# #to continue in the same line
# print('hello ', end='')
# print('world')
# #Comma can be seen in output with sep
# print('cats', 'dogs', 'mice')
# print('cats', 'dogs', 'mice', sep=',')

#2.2.Converting to String, Int, Float

# print('My age is ' + str(21))
# print(int('15') + 5)
# print(float('5.5') + 0.5)

#2.3 Illegal operations

#print(int('7.7'))  #wrong
# print(int(7.7))    #correct
# print(int('7'))    #correct

#2.4.Comparison Operators ==, !=. <, >, <=, >=, evaluates to True or False

# print(42 == '42') #False
# print(42 == 42.00)#True
# print(True == True) #True
# print('hello' == 'Hello') #False
# print('dog' != 'cat') #True

#2.5.Boolean Operators ((Binary Boolean (and, or)), not)
#Order( 1. not, 2. and 3. or)
# print(True and False)   #both conditions have to be met
# print(True or False)    #either of the conditions have to met
# print (not True)        #'double negative'

#2.6. Boolean & Comparison (Left expression first and then right)
# print((4<5) and (5<6))
# print ((1 == 1) or (2 == 3))

#3.0 Conditionals
#3.1if,elif,  else statement

# name = 'Nitya'
# sisName = 'Nikita'
# if name == 'Nitya':
#     print('correct')
#     if sisName == 'Nikita':
#         print('correctSis')
#     else:
#         print('incorrectSis')
# elif name == 'Usha':
#     print('incorrect')
# else:
#     print('None')

#3.2 Loop (while)

# age = 15
# while age < 20:
#     print(age)
#     age += 1

#3.2.1 Break statement
# age2 = 15
# while True:
#     print(age2)
#     age2 += 1
#     if age2 == 20:
#         break
#
# print('Age is finally 20')

#3.2.2 Continue statement

# age3 = 15
# while True:
#     if age3 == 16:
#        age3 += 1
#        continue
#     print(age3)
#     age3 += 1
#     if age3 == 20:
#         break
#
# print('Age is finally 20')

# 3.2.3 For Loop
#
# for i in range(10):           #prints 0-9
#     print(i)

# sum = 0
# for i in range(101):          #Sum of 0-100
#     sum += i
#
# print(sum)


# sum1 = 0
# i1 = 0
# while i1 < 101:               #the above for loop as a while loop
#     sum1 += i1
#     i1 += 1
#
# print(sum1)

#3.2.4 For loop (start, stop, step)

# for j in range(10,20):        //creates a list from starting from 10 and goes upto 19
#     print(j)

# for k in range(10, -20, -2):
#     print(k)
#
#
#3.2.5 Import Library
#
# import random, math
#
# for i in range(1,10):
#     print(random.randint(1,i))

# from random import *
#
# for i in range(1,10):
#     print(randint(1,i))

# from sys import *
#
# while True:
#     print('Name?')
#     name = input()
#     if name == 'Nikita':
#         print('correct')
#         exit()
#     else:
#         print('Retry')


# Infinite While loop
# while True:
#     print(5)

