"""
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
    3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem6(nat):
    su = sq = 0
    for i in range(1,nat+1,1):
        su += i**2
        sq += i
    return sq**2 - su

#nat = 10
nat = 100
print(problem6(nat))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#answer is 25164150