# Created by Kenneth Sweezy
# Yes, I know, not the most efficient thing in the world

import sys
import time
from colorama import init, Fore
init()


temp = 0

# Possible characters for inputs in each column
firstColumnChars = ['a','b','c','e','f','g','h','l','n','o','p','r','s','t','w']
secondColumnChars = ['b', 'f', 'g', 'e', 'v', 'o', 'i', 'r', 'a', 't', 'l', 'm', 'p', 'h']
thirdColumnChars = ['a', 'e', 'g', 'h', 'i', 'l', 'o', 'r', 't', 'u', 'v']
fourthColumnChars = ['a', 'c', 'd', 'e', 'g', 'h', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']
fifthColumnChars = ['d', 'e', 'g', 'h', 'k', 'l', 'n', 'r', 't', 'w', 'y']

# Possible words for each starting letter
possibleA = ['about', 'after', 'again']
possibleB = ['below']
possibleC = ['could']
possibleE = ['every']
possibleF = ['first', 'found']
possibleG = ['great']
possibleL = ['large', 'learn']
possibleN = ['never']
possibleO = ['other']
possibleP = ['place', 'plant', 'point']
possibleR = ['right']
possibleS = ['small', 'sound', 'spell', 'still', 'study']
possibleT = ['their', 'there', 'these', 'thing', 'think', 'three']
possibleW = ['water', 'where', 'which', 'world', 'would', 'write']

# All possible words
allPossible = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'large', 'learn', 'never',
               'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there',
               'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

# Words Possible after firstColumn check
firstPossible = []

# Words Possible after secondColumn check
secondPossible = []

# Words Possible after thirdColumn check
thirdPossible = []

# Words Possible after fourthColumn check
fourthPossible = []

# Input and checks for the firstColumn
firstColumn = raw_input('Please enter the characters for the first column: ' + Fore.YELLOW)

for char in firstColumn:
    if char in firstColumnChars:
        temp += 1
    else:
        print(Fore.LIGHTRED_EX + char + Fore.RED + ' is not a valid first character.')
if temp == 5:
    print(Fore.GREEN + 'All values entered are possible first characters.' + Fore.RESET)
    temp = 0
else:
    print(Fore.RED + 'There is an incorrect number of characters entered.' + Fore.RESET)
    temp = 0
    #sys.exit()

# Input and checks for the secondColumn
secondColumn = raw_input('Please enter the characters for the second column: ' + Fore.YELLOW)

for char in secondColumn:
    if char in secondColumnChars:
        temp += 1
    else:
        print(Fore.LIGHTRED_EX + char + Fore.RED + ' is not a valid second character.')
if temp == 5:
    print(Fore.GREEN + 'All values entered are possible second characters.' + Fore.RESET)
    temp = 0
else:
    print(Fore.RED + 'There is an incorrect number of characters entered.' + Fore.RESET)
    temp = 0
    #sys.exit()

# Input and checks for the thirdColumn
thirdColumn = raw_input('Please enter the characters for the third column: ' + Fore.YELLOW)

for char in thirdColumn:
    if char in thirdColumnChars:
        temp += 1
    else:
        print(Fore.LIGHTRED_EX + char + Fore.RED + ' is not a valid third character.')
if temp == 5:
    print(Fore.GREEN + 'All values entered are possible third characters.' + Fore.RESET)
    temp = 0
else:
    print(Fore.RED + 'There is an incorrect number of characters entered.' + Fore.RESET)
    temp = 0
    #sys.exit()

# Input and checks for the fourthColumn
fourthColumn = raw_input('Please enter the characters for the fourth column: ' + Fore.YELLOW)

for char in fourthColumn:
    if char in fourthColumnChars:
        temp += 1
    else:
        print(Fore.LIGHTRED_EX + char + Fore.RED + ' is not a valid fourth character.')
if temp == 5:
    print(Fore.GREEN + 'All values entered are possible fourth characters.' + Fore.RESET)
    temp = 0
else:
    print(Fore.RED + 'There is an incorrect number of characters entered.' + Fore.RESET)
    temp = 0
    #sys.exit()

# Input and checks for the fifthColumn
fifthColumn = raw_input('Please enter the characters for the fifth column: ' + Fore.YELLOW)

for char in fifthColumn:
    if char in fifthColumnChars:
        temp += 1
    else:
        print(Fore.LIGHTRED_EX + char + Fore.RED + ' is not a valid fifth character.')
if temp == 5:
    print(Fore.GREEN + 'All values entered are possible fifth characters.' + Fore.RESET)
    temp = 0
else:
    print(Fore.RED + 'There is an incorrect number of characters entered.' + Fore.RESET)
    temp = 0
    #sys.exit()

print(Fore.LIGHTGREEN_EX + 'All of these characters are correct, and will result in a correct word.' + Fore.RESET)

# Fancy "loading" animation
print(Fore.CYAN + 'Calulating word'),
time.sleep(0.5)
print('.'),
time.sleep(0.5)
print('.'),
time.sleep(0.5)
print('.')

# Removes words starting in "a"; if "a" is not in firstColumn
if 'a' in firstColumn:
    if 'b' in secondColumn:
        firstPossible.append('about')
    if 'f' in secondColumn:
        firstPossible.append('after')
    if 'g' in secondColumn:
        firstPossible.append('again')
# Removes words starting in "b"; if "b" is not in firstColumn
if 'b' in firstColumn:
    if 'e' in secondColumn:
        firstPossible.append('below')
# Removes words starting in "c"; if "c" is not in firstColumn
if 'c' in firstColumn:
    if 'o' in secondColumn:
        firstPossible.append('could')
# Removes words starting in "e"; if "e" is not in firstColumn
if 'e' in firstColumn:
    if 'v' in secondColumn:
        firstPossible.append('every')
# Removes words starting in "f"; if "f" is not in firstColumn
if 'f' in firstColumn:
    if 'i' in secondColumn:
        firstPossible.append('first')
    if 'o' in secondColumn:
        firstPossible.append('found')
# Removes words starting in "g"; if "g" is not in firstColumn
if 'g' in firstColumn:
    if 'r' in secondColumn:
        firstPossible.append('great')
# Removes words starting in "h"; if "h" is not in firstColumn
if 'h' in firstColumn:
    if 'o' in secondColumn:
        firstPossible.append('house')
# Removes words starting in "l"; if "l" is not in firstColumn
if 'l' in firstColumn:
    if 'a' in secondColumn:
        firstPossible.append('large')
    if 'e' in secondColumn:
        firstPossible.append('learn')
# Removes words starting in "n"; if "n" is not in firstColumn
if 'n' in firstColumn:
    if 'e' in secondColumn:
        firstPossible.append('never')
# Removes words starting in "o"; if "o" is not in firstColumn
if 'o' in firstColumn:
    if 't' in secondColumn:
        firstPossible.append('other')
# Removes words starting in "p"; if "p" is not in firstColumn
if 'p' in firstColumn:
    if 'l' in secondColumn:
        if 'a' in thirdColumn:
            if 'c' in fourthColumn:
                firstPossible.append('place')
            if 'n' in fourthColumn:
                firstPossible.append('plant')
    if 'o' in secondColumn:
        firstPossible.append('point')
# Removes words starting in "r"; if "r" is not in firstColumn
if 'r' in firstColumn:
    if 'i' in secondColumn:
        firstPossible.append('right')
# Removes words starting in "s"; if "s" is not in firstColumn
if 's' in firstColumn:
    if 'm' in secondColumn:
        firstPossible.append('small')
    if 'o' in secondColumn:
        firstPossible.append('sound')
    if 'p' in secondColumn:
        firstPossible.append('spell')
    if 't' in secondColumn:
        if 'i' in thirdColumn:
            firstPossible.append('still')
        if 'u' in thirdColumn:
            firstPossible.append('study')
# Removes words starting in "t"; if "t" is not in firstColumn
if 't' in firstColumn:
    if 'h' in secondColumn:
        if 'e' in thirdColumn:
            if 'i' in fourthColumn:
                firstPossible.append('their')
            if 'r' in fourthColumn:
                firstPossible.append('there')
            if 's' in fourthColumn:
                firstPossible.append('these')
        if 'i' in thirdColumn:
            if 'n' in fourthColumn:
                if 'g' in fifthColumn:
                    firstPossible.append('thing')
                if 'k' in fifthColumn:
                    firstPossible.append('think')
        if 'r' in thirdColumn:
            firstPossible.append('three')
# Removes words starting in "w"; if "w" is not in firstColumn
if 'w' in firstColumn:
    if 'a' in secondColumn:
        firstPossible.append('water')
    if 'h' in secondColumn:
        if 'e' in thirdColumn:
            firstPossible.append('where')
        if 'i' in thirdColumn:
            firstPossible.append('which')
    if 'o' in secondColumn:
        if 'r' in thirdColumn:
            firstPossible.append('world')
        if 'u' in thirdColumn:
            firstPossible.append('would')
    if 'r' in secondColumn:
        firstPossible.append('write')

# Prints all of the possible words based on the firstColumn test
print(firstPossible)