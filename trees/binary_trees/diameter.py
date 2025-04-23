class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def diameter(root) -> int:
            if root is None:
                return 0
            
            lh = diameter(root.left)
            rh = diameter(root.right)

            current_diameter = lh + rh
            nonlocal max_diameter
            max_diameter = max(max_diameter, current_diameter)

            return 1 + max(lh, rh)
        
        diameter(root)
        return max_diameter