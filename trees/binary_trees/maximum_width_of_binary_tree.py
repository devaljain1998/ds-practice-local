# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        order = []
        queue = deque([(root, 0)])

        width = 0
        while queue:
            _sz = len(queue)
            min_idx = queue[0][1]

            first: int = -1
            last: int = -1
            for i in range(_sz):
                node, vertical_lvl = queue.popleft()
                cur_idx = vertical_lvl-min_idx

                if node.left is not None:
                    queue.append((node.left, 2*cur_idx))


                if node.right is not None:
                    queue.append((node.right, 2*cur_idx+1))
                
                # Assign first and last variables:
                if i == 0:
                    first = cur_idx
                
                if i == _sz-1:
                    last = cur_idx
            
            width = max(width, last - first + 1)
        
        return width

                
