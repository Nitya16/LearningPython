"""
--------------------------------------------------------
1. Dictionaries
a. { key: value, key: value..}
b. No ordering
--------------------------------------------------------
"""
print ('1. Common dictionary APIs keys() values() items() get(), setdefault()')

myDress = {'size': 'm','color': 'red', 'sleeves': 'short'}
print(myDress['size'])
print(myDress.keys())

print(myDress.values())
print(myDress.items())

print('Dress size is ' + myDress.get('size', 'unavail'))
print('Dress is from ' + myDress.get('shop', 'unknown') + ' shop')
print(myDress.setdefault('shop', 'H&M'))
print(myDress)

print ('\n2. Dict vs list?')
# Dictionaries have no order, for exact ordering, return the dict as a list() constructor function
for k in myDress.keys():
    print(k)

print(myDress.keys())
print(list(myDress.keys()))

print ('\n3. Check if a key exists in a dict?')
print('m' in myDress.keys()) # returns a Bool

if ('size' in myDress.keys()):
    print ('Yes, key exists')

print ('\n4. Insert into a dictionary and read')
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter the name of the person or enter nothing to exit')
    name = input()
    
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + 'is on ' + name)
    else:
        print(name + ' is not available!')
        print('what is the bday?')
        bday = input()
        birthdays[name]= bday
        print('Updated our dictionary')

print(birthdays)

print ('\n5. Pretty printing dictionaries')
# Module pprint ->  pprint() pformat() for pretty printing
import pprint

# Both are equal below
pprint.pprint(myDress)
print(pprint.pformat(myDress))
