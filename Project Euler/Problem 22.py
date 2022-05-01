
"""
https://projecteuler.net/problem=22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?

"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem22(file):
    sortedlist = file.read().replace("\"","").split(",")
    sortedlist.sort()
    total = count = 0
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #print(len(alphabet)) #making sure all 26 letters are in
    for eachword in sortedlist:
        letters = list(eachword)
        count += 1
        wordtotal = 0
        for eachletter in letters:
            wordtotal += alphabet.index(eachletter.lower())+1
        total += (wordtotal * count)
    return total


dir_path = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(dir_path,"p022_names.txt")
file = open(file, "r")

print(problem22(file))

#print(file)
print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is 871198282

