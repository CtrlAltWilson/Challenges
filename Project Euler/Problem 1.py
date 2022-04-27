#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

def problem1(max):
    result = 0
    for i in range(max):
        if (i%3 == 0 or i%5 == 0):
            result += i
    return result
    
max = 1000
print(problem1(max))

#answer is 233168