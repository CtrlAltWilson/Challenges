"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
#####################################
#                                   #
#      Incomplete, will return      #
#                                   #
#####################################
import os
import time

start_time = time.time()
clear = lambda: os.system('cls')
clear()

def problem7(num,limit):
    s = [2]
    buffer = [3,5,7,11,13]
    counter = 1
    for i in range(3,limit,2):
        if (i%3 != 0 and i%5 != 0 and i%7 != 0 and i%11 != 0 and i%13 != 0) or i in buffer: #this can be optimized
            counter += 1
            print("{}. {}".format(counter,i))
            if counter == num:
                return i
    return 0

num = 10001
limit = num**2
print(problem7(num,limit))

print("--- {} seconds ---".format(time.time() - start_time))
print("\n\n")

#answer is 104743