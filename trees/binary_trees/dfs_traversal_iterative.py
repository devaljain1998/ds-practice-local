from typing import List, Optional
from trees.binary_trees.tree_node import TreeNode
from collections import deque


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        order = []
        stack = deque([root])
        
        while stack:
            node = stack.pop()
            order.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        
        return order

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        order = []
        stack = deque()
        
        node = root
        while True:
            # Keep pushing the left elements into stack
            # until node is not None
            if node is not None:
                stack.append(node)
                node = node.left
            # if node is not none, then pop the stack
            # and then go to the left
            else:
                # if stack is empty then break
                if len(stack) == 0:
                    break
                node = stack.pop()
                order.append(node.val)
                node = node.right
        
        return order


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        node = root
        stack = deque()
        while True:
            # if node is there:
            if node is not None:
                stack.append(node)
                node = node.right
            # if node is null now
            # then go the right
            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                order.append(node.val)
                node = node.left
                
        return order