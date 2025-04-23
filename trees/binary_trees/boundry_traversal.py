#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def leftBoundry(self, root) -> list[int]:
        if root is None or (root.left is None and root.right is None):
            return []
            
        ans = []
        node = root
        while node:
            # check it should not be a leaf node:
            if not (node.left is None and node.right is None):
                ans.append(node.data)
                
            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                break
            
        return ans

    
    def leafNodes(self, root) -> list[int]:
        ans = []
        
        def inorder(root):
            if root is None:
                return
            # leaf node
            elif root.left is None and root.right is None:
                ans.append(root.data)
            
            inorder(root.left)
            inorder(root.right)
        
        inorder(root)
        return ans
    
    def rightNodes(self, root) -> list[int]:
        if root is None or (root.left is None and root.right is None):
            return []
            
        ans = []
        node = root.right
        while node:
            # check it should not be a leaf node:
            if not (node.left is None and node.right is None):
                ans.append(node.data)
                
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                break
            
        return ans
            
    
    def boundaryTraversal(self, root):
        # Handle edge cases
        if root is None:
            return []
        
        # Handle the case of a single node (just the root)
        if root.left is None and root.right is None:
            return [root.data]
        
        # Start with root
        order = [root.data]
        
        # Get left boundary (excluding root)
        left_boundary = self.leftBoundry(root.left)
        order.extend(left_boundary)
        
        # Get all leaf nodes
        leaf_nodes = self.leafNodes(root)
        order.extend(leaf_nodes)
        
        # Get right boundary in reverse order (excluding root)
        right_boundary = self.rightNodes(root)
        right_boundary.reverse()  # Reverse the right boundary nodes
        order.extend(right_boundary)
        
        return order
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{
#  Driver Code Starts
import sys

import sys

sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        res = obj.boundaryTraversal(root)
        for i in res:
            print(i, end=" ")
        print('')
        print("~")

# } Driver Code Ends