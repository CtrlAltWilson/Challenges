"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt
import os
import time

start_time = time.time()

def loading(i):
    i = i%10 #this gets the last digit of the number
    symbol = ['/','/','/','|','|','|','\\','\\','\\','\\']
    return "loading {}".format(symbol[i])

def problem3(max):
    s = []
    while max % 2 == 0:
        s.append(2)
        max = max/2
    for i in range(3,int(sqrt(max)),2):
        print("{} {}".format(loading(i),i))
        clear = lambda: os.system('cls')
        clear()
        if i > max:
            break
        while max%i == 0:
            s.append(i)
            max=max/i
    print(s)
    return s[len(s)-1]

max = 600851475143
#max = 13195
print("Largest prime factor for {} is {}".format(max,problem3(max)))
print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#answer is 6857