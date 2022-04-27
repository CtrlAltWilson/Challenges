"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem5(div, limit):
    for i in range(2,limit,2):
        counter = 1
        while i%counter == 0:
            counter += 1
            if counter == div:
                return i
    return 0

div = 20
limit = 99999999999
print(problem5(div,limit))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#answer is 232792560