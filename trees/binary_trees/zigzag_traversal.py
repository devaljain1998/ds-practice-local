from collections import deque
from typing import List, Optional

from trees.binary_trees.tree_node import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        queue = deque()
        if root is not None:
            queue.append(root)
        
        left_to_right_flag = True
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
                if left_to_right_flag:
                    order.append(temp)
                else:
                    temp.reverse()
                    order.append(temp)
            left_to_right_flag = not left_to_right_flag
        
        return order
