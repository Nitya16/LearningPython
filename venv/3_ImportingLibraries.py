"""
--------------------------------------------------------
1. Importing Libraries
--------------------------------------------------------
a. import x
b. from x import *
"""

print ('1. Importing library header only (like say just the index of a book)')
import random

for i in range(1,10):
    print(random.randint(1,i))

print ('\n2. Importing full library (like all chapters of the book)')
from random import *

for i in range(1,10):
    print(randint(1,i))

from sys import *

while True:
    print('Name?')
    name = input()
    if name == 'Nikita':
        print('correct')
        exit()
    else:
        print('Retry')

print('Hi')     #Difference between break vs exit()
