
"""
https://projecteuler.net/problem=14
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

"""

from math import sqrt
import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem14(limit):
    largest = larCount = 0
    for i in range(int(limit/2),limit,1): #we don't need to start from the bottom if we are looking for the largest chain, let's start elsewhere
        num = i
        counter = 0
        while num != 1:
            if num%2 == 0:
                num /= 2
            else:
                num = 3*num+1
            counter +=1
        if counter > larCount:
            largest = i
            larCount = counter
    return "Starting chain {} has the longest chains at {} chains".format(largest,larCount)

limit = 1000000
print(problem14(limit))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is 837799

