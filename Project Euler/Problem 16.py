
"""
https://projecteuler.net/problem=16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Warning, this question contains Sup
"""

import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem16(pow):
    num = 2**pow
    s = list(str(num))
    sum = 0
    for i in s:
        sum += int(i)
    return sum

pow = 1000
print(problem16(pow))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#Answer is 1366

