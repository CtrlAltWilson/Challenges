"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem9(num):
    for i in range(1, int(num/3)+1):
        for j in range(i+1,int(num/2)+1):
            k = num - i - j
            if (i**2 + j**2 == k**2):
                print("a = {}, b = {}, c = {}".format(i,j,k))
                return i*j*k
    return 0

num = 1000
print(problem9(num))


print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is 31875000