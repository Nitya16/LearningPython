

from pyperclip import *
#Step1: Copy data from clipboard


input= paste()
print(input)



#Step2: Add bullets to data


output = input.split('\n')
final = ''
for i in range(len(output)):
    output[i] = '* ' + output[i]
answer= ('\n'.join(output))




#Step3: Paste the data back to clipboard

copy(answer)
