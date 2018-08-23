"""
--------------------------------------------------------
1. Variable Scopes
a. Local scope
b. Global scope
--------------------------------------------------------
"""

print ('1. Local scopes cannot use variables in other local scopes')
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(eggs)

spam()
''' Every method has its own local scope. So here
# spam method
{
    spam's local variable eggs = 99
    Bacon()
    {
        bacon's local variable eggs = 0
    }
    
    eggs = 99
}
}
'''

print ('\n2. Global variables can be read from local scope')

def spam():
    print(eggs)

eggs = 42 #Globally scoped variable

spam()
print(eggs)

print ('\n3. Local and Global variables can have the same name')
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global
print(eggs)
spam()
print(eggs)
