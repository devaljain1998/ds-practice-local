from collections import deque
from typing import List, Optional
from trees.binary_trees.tree_node import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        order = []
        queue = deque([root])
        
        while queue:
            _sz = len(queue)
            temp = []
            while _sz > 0:
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)
                
                _sz -= 1
            
            if temp:
                order.append(temp)
        
        return order
