
print ('\n1.Finding Patterns of text from input')

def isPhoneNumber(text):
    # (404-820-3158)
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

input1= '404-820-3158'
input2='This is 404-820-3158 not a number'
print(isPhoneNumber(input1))
print(isPhoneNumber(input2))


print ('\n2. Finding a phone number in a text using patern matching')

finalAns=''
message= 'Call me at 404-820-3158. And later call in 803-424-5328!'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        finalAns= finalAns + '\n' + chunk

        # print('Phone number found: ' + chunk)
        print(finalAns)

print('Done')

print('\n3. Regex: Methods-> re.compile(), search(), group(), findall()')
print('re.compile():returns a Regex pattern objects')
print('search()    :returns None if no patter or returns Match object')
print('group()     :returns the matched object found in search()')
print('findall()   : Will find all possible matches and Has two use case')
print('\ta.Regex with no groups returns as list of strings')
print('\tb.Regex with grouos returns as list of tuples')
import re
print('Here d means a digit character: \d{3}-\d{3}-\d{4}')


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('\nPhone number found: ' + mo.group())
mofind = phoneNumRegex.findall('My number is 415-555-4242 and also 404-820-3258')
print('No grouping findall Method')
print(mofind)

print('\n4.Grouping with Paranthesis')
newNum = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
newMo= newNum.search('My num is: (404) 820-3158')
mofindG = newNum.findall('My number is (415) 555-4242 and also (404) 820-3258')
print('Grouping findall Method results in tuples within list')
print(mofindG)
print('.group(1): ' +newMo.group(1))
print('.group(2): ' +newMo.group(2))
print('.group(0): ' + newMo.group(0))
print('.groups() prints tuple list of groups ' )
print(newMo.groups())
print('Groups are listed as tuples and can hence use assignment')
areaCode, mainNum = newMo.groups()  #Can't assign to function call (Don't do opposite)
print('AreaCode:' +  areaCode)
print('Main Number: '+ mainNum)

print('\n5.Matching with Pipe-> | is called a pipe-> acts as OR-> Returns first occurence')
print('1.First determine the patern you want to search for')
print('2.Use the patern and search it in your given string')
print('3.Return the matched patern on string using group()')
print('Note: Case sensitive')
print('Example 1: Simple understanding of pipe matching')
sister = re.compile(r'Nitya|Nikita')
mo1= sister.search('Nitya and Nikita are sisters')
print(mo1.group())
print('\nExample 2: Deals with prefix, still captures first occurence')
fam = re.compile(r'Govind(Usha|Govindan|Nikita|Nitya)')
mo2= fam.search('GovindUsha, GovindNikita are related')
print(mo2.group())

print('\n6.Optional Matching with ?')
print('Def: Finding a match whether it exists or not')
print('Matches zero or one of the group preceeding the ?')

fam1= re.compile(r'GovindNi(kita)?')
mo3= fam1.search('Where is GovindNitya')
print(mo3.group())

print('\n7.Match 0 or more with *')
print('Def: can be absent or can occur multiple times')
batRegex = re.compile(r'Bat(wo)*man')
mo4 = batRegex.search('The Adventures of Batman')
mo5 = batRegex.search('Batwowowowoman')
print('Matching zero instance:')
print(mo4.group())
print('Matching multiple instance:')
print(mo5.group())

print('\n8.Match 1 or more with +')
print('Def: match 1 or more')

batRegex = re.compile(r'Bat(wo)+man')
mo6 = batRegex.search('The Adventures of Batwoman') #Match 1
mo7 = batRegex.search('The Adventures of Batwowowoman') #Match more than 1
mo8 = batRegex.search('The Adventures of Batman') #Match 0

print(mo6.group())
print(mo7.group())
print(mo8 == None)  #Won't return anything, you have to ask for Boolean Value

print('\n9.Matching specific repetitions with {}')
print('Def: {start,stop} ->both included-> if no bounds will start from extremes')
print('\nGreedy Group Example (Default: Longest string)')
haRegex = re.compile(r'(Ha){3}')
mo9 = haRegex.search('HaHaHa')
print(mo9.group())

mo10 = haRegex.search('Ha')
print(mo10 == None)

print('\nNon-Greedy Group Example (?: shortest string return)')
haRegex = re.compile(r'(Ha){3,5}?')
mo11 = haRegex.search('HaHaHaHaHa')
print(mo11.group())

print('\n10.Character Classes')
print('\d digits, \D non digits, \w word characs, \W non woed char, \s space or tab, \S Non space or tab')

christmasList = re.compile(r'\d+\s\w+')
finalList= christmasList.findall('11 birds and 5 sheeps with 8 dogs or 99 cats where 67 bears')
print(finalList)

print('\tMake your own Character Class use [] brackets: Vowel example[aeiouAEIOU]')
print('\tInside [] no need of escape chars, viewed as raw')
print('\tcan also contain [a-zA-Z0-9]')
print('\tUsing ^ will match the negative char class: Vowel example[^aeiouAEIOU] will match consonents')

print('\n11.Strict Matching: Carots (^start) costs Dollars ($end)')
print('\n12.Wildcard (.) :Will match one char more than specified without newline')
print('\n13.DotStar Greedy(<.*>) Non-greedy(<.*?>')
print('\n14.For newline: (.*, re.DOTALL)')
print('\n14.For case-insenstive: (nitya, re.I)')
print('\n15. Sub-Method: Go over')
print('\tComplex Regex can be written in multiple lines using triple quotes')






