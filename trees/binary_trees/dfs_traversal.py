from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        
        def preorder_dfs(root: Optional[TreeNode]):
            if root == None:
                return
            
            order.append(root.val)
            preorder_dfs(root.left)
            preorder_dfs(root.right)
        
        preorder_dfs(root)
        return order

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    order = []
    
    def inorder_dfs(root: Optional[TreeNode]):
        if root == None:
            return
        
        inorder_dfs(root.left)
        order.append(root.val)
        inorder_dfs(root.right)
    
    inorder_dfs(root)
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