"""
Problem Description
There are many cars parked in the parking lot. The parking space is a long straight line, with one parking space per meter. Many cars are currently parked, and you want to shelter from the rain by building a roof. It is required that at least the roofs of k cars are covered by the roofs. What is the minimum length to cover the roofs of k cars?
This function has the following parameters:

cars: an integer array of length, representing the parking space for parking cars
k: Integer, indicating the number of cars that must be covered by the roof
Sample
Example:
Input:
cars: [2, 10, 8, 17]
k: 3
Output: 9
Explanation: You can build a roof with a length of 9 to cover all parking spaces from the 2nd to the 10th, so you can cover 3 cars at the 2nd, 10th, and 8th positions. There is no shorter one that can cover the roof of 3 cars, so the answer is 9

Precautions
1 <= n <= 10^5
1 <= k <= n
0 <= cars[i] <= 10^14
The cars above all parking spaces are unique

"""

def parking(cars, k):
    cars.sort()
    result = float("inf")
    print(cars)
    for i in range(len(cars) - k + 1):
        print(i, cars[i+k-1],cars[i]+1,cars[i+k-1] - cars[i]+1)
        result = int(min(result,cars[i+k-1] - cars[i]+1))
    return result

cars = [2, 10, 8, 17]
k = 3
print(parking(cars,k))