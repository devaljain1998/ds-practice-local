class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float('-inf')

        def helper(node) -> int:
            if node is None:
                return 0
            
            # Calculate max path sum from left and right subtrees
            # Take max of the sum and 0 to handle negative values
            ls = max(0, helper(node.left))    # Ignore negative contributions
            rs = max(0, helper(node.right))   # Ignore negative contributions

            nonlocal maxsum
            # Update global max with current node's best path
            maxsum = max(maxsum, node.val + ls + rs)
            
            # Return max path sum ending at this node (for parent's calculation)
            return node.val + max(ls, rs)
        
        helper(root)
        return maxsum