
"""
https://projecteuler.net/problem=24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

import os
import time


start_time = time.time()
clear = lambda: os.system('cls')
clear()

def verify(array,list):
    for i in list:
        if not i in array:
            return False
    return True
            


def problem24(num,limit):
    count = 362880
    current = 1234567880
    while count != limit:
    #while current != 1234567891:
#        print(current,count, num)
        current += 1
        splitnum = list(str(current))
        for i in range(0, len(splitnum)):
            splitnum[i] = int(splitnum[i])
        #print(splitnum,num)
        #print(splitnum)
        if verify(splitnum,num):
            count += 1
        #print(count)
    return current

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
limit = 1000000
print(problem24(num,1000000))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is 2783915460

