"""
--------------------------------------------------------
1. Operators
--------------------------------------------------------
a. What are operators?
-> +, -, /, *, //, **, %, =, and, or, not, ==, !=. <, >, <=, >=,
b. Operators follow what rules for precedence?
-> BO(Exponent)ModulusDMAS rule (**, * / //, %, + -)
-> What is //? -> Integer Division i.e. 22//8 = 6)
"""

"""
--------------------------------------------------------
2. Data Types
--------------------------------------------------------
a. What are the different data types Python uses?
-> int, float, str , none, list
b. What is None? Where is it used?
-> It is basically assigning nothing.
"""

# Example 1: Data type 'None' usage - to identify if something has touched your variable
print ('1. Learning None data type.')
def connectToDatabase():
    return

myVariable = None

myVariable = connectToDatabase()
#If myVariable = 5 proceed to else
if (None == myVariable):
    print ('Nothing changed myVariable. This means we couldn\'t connect to the database')
else:
    print ('Something changed myVariable. This means we could connect to the database! Yahoo!')

# None also indicates the return type of methods that return nothing
returnTypeVariable = print('What is the return type of the method print(arg)? Is it None?')
print (None == returnTypeVariable)

# Example 2: Converting Int/Float -> String
print ('\n2. Learning data type conversions.')
print('My age is ' + str(21))
print('My weight is ' + str(21.1))
# Example 2.1: Converting String -> Int/Float
print(int('15') + 5)
print(float('5.5') + 0.5)
# Example 2.2: Converting Float -> Int
print(int(7.7))
# Example 2.3: ILLEGAL: Converting String (which encloses a Float) -> Int
#print(int('7.7'))  #wrong
print ('\n3. Learning data types and operators.')
# Example 2.4:
print(42 == '42') #False
print(42 == int('42'))
#print(42 == int('42.00'))  Illegal
print(42 == 42.00) #True
print(True == True) #True
print('hello' == 'Hello') #False bec it is case-sensitive
print('dog' != 'cat') #True
print(True and False)   #both conditions have to be met
print(True or False)    #either of the conditions have to met
print (not True)        #'double negative'
print((4<5) and (5<6)) #True
print ((1 == 1) or (2 == 3)) #True

print ('\n2. Learning String Formatting')
print("Hello there!\nHow are you?\nI\'m doing fine.")
print(r'That is Carol\'s cat.') #This is a raw string
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')