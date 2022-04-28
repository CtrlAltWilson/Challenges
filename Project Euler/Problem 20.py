
"""
https://projecteuler.net/problem=20
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem20(num):
    s = num
    for i in range(num-1,1,-1):
        s *= i
    l = list(str(s))
    sum = 0
    for i in l:
        sum += int(i)
    return sum

num = 100
print(problem20(num))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is 648

