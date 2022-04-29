import bisect
from os import system
clear = lambda: system('cls')
clear()

class MyCalendar:
    def __init__(self):
        self.times = []
        self.bool = []

    def book(self, start: int, end: int) -> bool:
        for i in self.times:
            if (i[0] <= start < i[1]) or \
                (i[0] < end <= i[1]) or \
                (start <= i[0] and end >= i[1]):
                self.bool.append(False)
                return False
        scheduled = [start,end]
        self.times.append(scheduled)
        #print(self.times)
        self.bool.append(True)
        return True
    def getMatch(self):
        return (self.bool)
"""
        if end <= start:
            return False
        i = bisect.bisect_right(self.times, start)
        if i%2:
            return False
        j = bisect.bisect_left(self.times, end)
        if i!=j:
            return False
        print(i,j)
        
        self.times[i:j] = [start,end]
        return True
"""
myCalendar = MyCalendar()
true = True
false = False
#inp =[[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
#expected = [true,true,false,false,true,false,true,true,true,false]
#inp =[[37,50],[33,50],[4,17],[35,48],[8,25]]
#expected = [true,false,true,false,false]
#inp =[
#    [20,29],[13,22],[44,50],[1,7],  [2,10], 
#    [14,20],[19,25],[36,42],[45,50],[47,50],
#    [39,45],[44,50],[16,25],[45,50],[45,50],
#    [12,20],[21,29],[11,20],[12,17],[34,40],
#    [10,18],[38,44],[23,32],[38,44],[15,20],
#    [27,33],[34,42],[44,50],[35,40],[24,31]]
#expected = [true,false,true,true,false,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
inp = [
    [97,100],[33,51],[89,100],[83,100],[75,92],
    [76,95],[19,30],[53,63],[8,23],[18,37],
    [87,100],[83,100],[54,67],[35,48],[58,75],
    [70,89],[13,32],[44,63],[51,62],[2,15]]
expected = [true,true,false,false,true,false,true,true,false,false,false,false,false,false,false,false,false,false,false,true]
for i in inp:
    myCalendar.book(i[0],i[1])
result = myCalendar.getMatch()
#print("1. ",result)
#print("2. ",expected)
print(myCalendar.getMatch() == expected)
 
errormatch = [[],[]]
noreturn = 0
for i in range(len(expected)):
    if expected[i] != result[i]:
        if len(errormatch) == 2 and noreturn == 0:
            errormatch = ([i+1,inp[i]])
            noreturn = 1
        else:
            errormatch.append([i+1,inp[i]])
if errormatch != [[],[]]:
    print(errormatch)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)