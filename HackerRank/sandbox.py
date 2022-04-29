
#TREES
"""
INORDER TRAVERSAL
def levelOrder(root):
    s = []
    def getOrder(root):
        if not root:
            return
        getOrder(root.left)
        s.append(root.info)
        getOrder(root.right)
        
        #print (s)
    getOrder(root)
    print ("Result"," ".join(map(str,s)))
    return " ".join(map(str,s))
"""

"""
HEIGHT OF TREE
def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)
    return 1+max(left_height, right_height)   
"""

"""
TRAVERSE LEVEL ORDER TREE

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
"""