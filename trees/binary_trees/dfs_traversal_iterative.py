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
        stack = deque([root])
        
        while stack:
            node = stack.pop()
            
                
        return order

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        
        def postorder_dfs(root: Optional[TreeNode]):
            if root == None:
                return
            
            postorder_dfs(root.left)
            postorder_dfs(root.right)
            order.append(root.val)
        
        postorder_dfs(root)
        return order