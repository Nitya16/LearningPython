"""
--------------------------------------------------------
1. Conditionals
--------------------------------------------------------
a. if: elif: else:
b. while condition:
c. break:
d. continue:
e. exit()
f. for i in range(stop) // default start = 0, step = 1
for i in range(start,stop) 
for i in range(start,stop,step)
"""

# Example 1: if: elif: else:
print ('1. Learning if: elif: else')
name = 'Nitya'
sisName = 'Nikita'
if name == 'Nitya':
    print('correct')
    if sisName == 'Nikita':
        print('correctSis')
    else:
        print('incorrectSis')
elif name == 'Usha':
    print('incorrect')
else:
    print('None')

# Example 2: while condition:
print ('\n2. Learning while condition')
age = 15
while age < 20:
    print(age)
    age += 1

# Infinite While loop
# while True:
#     print(5)

# Example 3: break:
print ('\n3. Learning break statement')
age2 = 15
while True:
    print(age2)
    age2 += 1
    if age2 == 20:
        break

print('Age is finally 20')

# Example 4: continue:
print ('\n4. Learning continue statement')

age3 = 15
while True:
    if age3 == 16:
        age3 += 1
        continue
    print(age3)
    age3 += 1
    if age3 == 20:
        break

print('Age is finally 20')

# Example 5: sys.exit()
from sys import *

while True:
    print('Name? (Hint: Nikita')
    name = input()
    if name == 'Nikita':
        print('correct')
        exit()
    else:
        print('Retry')

# Example 6: for:
# For loops basically generate a list [] -> [start, stop -1]
# eg. range (10) -> [0,1,2,3,4,5,6,7,8,9]
# eg. range (10,11) -> [10]
# eg. range (10,10) -> []
# eg. range (10,-10) -> [] // cannot start with 10 and be < -10.
print ('\n5. Learning for loop')

print ('print 0-9')
for i in range(10):
    print(i)

print ('sum of 0-100')
sum = 0
for i in range(101):
    sum += i

print(sum)

print ('sum of 0-100 using while loop')
sum1 = 0
i1 = 0
while i1 < 101:
    sum1 += i1
    i1 += 1

print(sum1)

print ('print 10-19')
for j in range(10,20):
    print(j)

print ('print 10- -18 in steps of 2')
for k in range(10, -20, -2):
    print(k)

print ('print 10-10')
for k1 in range(10, 10):
    print(k1)

print ('print 10- -10')
for k2 in range(10, -10):
    print(k2)
