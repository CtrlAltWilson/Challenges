############################
#
# DUMP TEST CODES HERE
#
############################


#DICTIONARY
#p = ([1,2,3,{'apple': 52,'banana':25}])
#print(p[3]["apple"])


#s = {"apple":52, "banana":25}
#print (s["apple"])
#s.pop('banana',None)
#del s['apple']
#print(s)

#s = [1, 2, 3, 4, 5]
#print(sum(s[0:4]),sum(s[len(s)-4:len(s)]))
"""
time = '07:05:45PM'
newtime = time.split(":")
print()
print(":".join(newtime))
time3 = ":".join(newtime)
time3 = list(time3)
#print(time3)
time3.remove("P")
#time3.remove("M")
print(time3)
print(time.remove[len(time)-3:len(time)-1])
"""

def gettime(s):
    if "M" not in list(s):
        return s
    time = s.split(":")
    if "PM" in s:
        if int(time[0]) != 12:
            time[0] = str(int(time[0]) + 12)
    elif int(time[0]) == 12:
        time[0] = str(int(time[0])-12)
    time[len(time)-1] = time[len(time)-1][0:2]
    time = ":".join(time)
    return time

s = ['11:05:45PM','05:05:45AM','12:05:45AM','13:00:00']
for i in s:
    print(gettime(i))
        

"""
graph = [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

for i, row in enumerate(graph):
    print(" ")
    for j, colmn in enumerate(graph[0]):
        print(graph[i][j])
        """