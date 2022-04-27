"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem4(digits):
    s = []
    a = []
    result = 0
    for i in range(digits):
        s.append(9)
    x = int(''.join(map(str,s)))
    for i in range(x,-1,-1): #x range of max to -1
        for j in range(x,-1,-1): #y range of max to -1
            #print("I = {}, J = {}\r".format(i,j), end="")
            test = i*j
            testarr = list(str(test))
            revtestarr = testarr[::-1] #reverse the dummy array and compare
            temp = int(''.join(map(str,testarr)))
            if revtestarr == testarr and temp > result:
                result = temp
                a = [i,j]
    return "The largest palindrome from {} digits is {} using {} and {}".format(digits,result,a[0],a[1])

digits = 3
print(problem4(digits))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#answer is 906609