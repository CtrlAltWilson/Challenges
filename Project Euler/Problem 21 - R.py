
"""
https://projecteuler.net/problem=21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem21(num):
    result = 0
    for i in range(1,num):
        if num%i == 0:
            result += i
    return result

num = 10000
print(problem21(num))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is 31626

