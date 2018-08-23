"""
--------------------------------------------------------
1. Lists and Tuples
--------------------------------------------------------
"""

print ('1. Ways to make and modify lists')
spam =[ 1, 2, 3]
spam2 =['cat', 'bat', 'rat', 'mat', ]
spam3 = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam)
print(spam2[1])      #1 is the index
print(spam3[1][0])  #[1]which list to use[0]which value to use
print (spam3[-1])   #Negative index gives you the last item in list

spam[1] = 6
print(spam)

spam[-1] = 10
print (spam)

del spam[-1]
print (spam)

concat = spam + spam2
print (concat)

print('check')
con= spam3 + spam
print(con)

replicate = spam * 3
print (replicate)

lslice = ['cat', 'bat', 'rat', 'elephant']
print(lslice[0:-1]) #[0 included in output:-1 excluded in output] #[defualt starts at 0: end is list length]
print(len(lslice))

# print ('\n2. Input all cat names in a list')
#
# cats = []
#
# while True:
#     print ('Current cats are ' + ':'.join(cats))
#     print("Please enter your cat's name or enter 'done' to quit, Cat")
#     answer = input()
#     print (answer)
#     if answer == "done":
#         break
#
#     cats = cats + [answer]
#
# print("The cat names are: ")
# for name in cats:
#         print(' '+ name)


print ('\n2. Looping through list, checking elements in list')
alphab = ['m','o','g','p','r' ]
for i in range(len(alphab)):
     print('Index '+ str(i) + ' is: ' + alphab[i])

anotherList = [1,2, 3, 4, 5]
for i in range(len(anotherList)):
     print('Index '+ str(i) + ' is: ' + str(anotherList[i]))



print('m' not in alphab) #False
print('34' in alphab) #False

# print ('\n3. Find pet in a list of pets')
#
# myPets = ['cat', 'dog', 'pig']
# myWrongPets =[]
#
# while(True):
#     print('Name your pet or enter \'exit()\' to leave: ')
#     answer = input()
#     if answer in myPets:
#         print(answer + " is your pet!")
#     else:
#         print(answer + " is not your pet")
#         myWrongPets= myWrongPets + [answer]
#         myWrongPets.append
#         break

#1.8 Multiple Assignmennt

dog =['small', 'brown', 'furry']
size, color, typed = dog
print(size,color)
#Shift?
# a , b = 1, 2
# a , b = b, a
# print(a, b)
#
# #1.9 Augmented Assignment (+=, -=, /=, *=)
# spam = 25
# spam+= 1
# print(spam) #can be done with strings too
#
print('\nMethods with Lists')
#2.0 Methods with Lists (index(), append(), insert(), remove(), sort(), sort()
print(dog.index('small'))   #FINDS the index value of the item in list
dog.append('red')           #ADDS a value to the END of list
print(dog)
dog.insert(1,'noisy')       #ADDS a value to the INDEX number (index, value)
print(dog)
dog.remove('noisy')         #REMOVES the value from list
print(dog)
 #NOTE: Use remove when you know the value and del statement when you know the index
del dog[3]
print(dog)
dog.sort()
print(dog)
#Note:
#1. On either alpha or numerical list not both
#2. To reverse use .sort(reverse=true)
#3. ASCII method used and hence Capital letters valued at first and then small
#4. If normal sort is required use .sort(key=str.lower)

############################### Magic 8 Ball ##############################

print('\nCreate magic 8 ball')

print('\n3.0 List like types:Strings and Tuples')
#3.1 Strings act a lot like lists
#it can do slice(), index(), for loop, len(), in, not in

name = 'Nitya'
print('Ni' in name)
print(name[1])

for i in name:
    print('*********' + i + '**********')
#Note: Strings are immutable, means it can't change except making a new string by slicing and concaranation
#Lists are mutable, can assign new value but only overwrites if you want to change use del() and append()

print('\n4.0 Tuples')
#3.2 Tuple () -> like lists but immutable
#
# print(type(('nitya',)))
#Note: Use when you don't want to alter list & tuples are faster than lists

# 3.3 Convertion
# print(tuple([name]))
# print(list((name)))
# print(str(name))

#3.5 Refrences: Changing list changes both the lists because both have same ref id

# 3.6 copy.copy() -> used to copy list or dictionary
#     copy.deepcopy() -> used to copy lists containing inner list
# import copy


#############################Character Picture Grid#############################
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
print(grid[2][1])

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='' )
    print()


