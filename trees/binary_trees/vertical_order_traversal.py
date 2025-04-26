from collections import defaultdict, deque
from typing import Optional, List, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        # Map: vertical -> list of (row, value)
        vertical_map = defaultdict(list)
        queue = deque([(root, 0, 0)])  # node, vertical, row

        while queue:
            node, vertical, row = queue.popleft()
            vertical_map[vertical].append((row, node.val))

            if node.left:
                queue.append((node.left, vertical - 1, row + 1))
            if node.right:
                queue.append((node.right, vertical + 1, row + 1))

        result = []
        for x in sorted(vertical_map.keys()):
            # Sort by row first, then value
            column = sorted(vertical_map[x])
            result.append([val for row, val in column])

        return result
