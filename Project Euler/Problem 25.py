
"""
https://projecteuler.net/problem=25
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

debug = 1

def problem25(num):
    term = 1
    for i in range(num-1): #for each digits
        term *= 10
    F = [0,1] #starting fibbo
    while F[len(F)-1] < term:
        if debug: print("{}".format(F.index(F[len(F)-1])))
        F.append(F[len(F)-1]+F[len(F)-2]) #add last with second last and append
    return F.index(F[len(F)-1])

num = 1000
print(problem25(num))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is

