class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return 1 + max(leftHeight, rightHeight)