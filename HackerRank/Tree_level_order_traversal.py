"""
question : https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
source : https://www.youtube.com/watch?v=MBZ-gBkjdMc&t=0s
"""
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
########################################################################################
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def levelOrder(root):
    if root is None:
        return []
    queue = [root]
    next_queue = []
    #level = [] <- option 1
    result = []
    while queue != []:
        for root in queue:
            #level.append(root.info) <- option 1 will create arrays in arrays 
            result.append(root.info) # <- option 2 will list all numbers
            if root.left is not None:
                next_queue.append(root.left)
            if root.right is not None:
                next_queue.append(root.right)
        #result.append(level) <-- should be with option 1
        #level = [] <- option 1
        queue = next_queue
        next_queue = []
    s = ""
    for i in result:
        s += "{} ".format(str(i))
    print (s)
    return s

#6
#1 2 5 3 6 4
#expected 1 2 5 3 6 4
########################################################################################
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)