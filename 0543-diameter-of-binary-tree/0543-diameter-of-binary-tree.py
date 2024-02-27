# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def dfs(n):
            if not n:
                return 0
            
            left_depth = 1 + dfs(n.left) if n.left else 0
            right_depth = 1 + dfs(n.right) if n.right else 0
            crt_max_depth = left_depth + right_depth
            
            nonlocal max_depth
            if crt_max_depth > max_depth:
                max_depth = crt_max_depth
                
            return max(left_depth, right_depth)
        
        dfs(root)
        
        return max_depth