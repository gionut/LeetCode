# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def treeSum(node):
            if node == None:
                return 0
            
            descSum = treeSum(node.left) + treeSum(node.right)
            
            if node.val == descSum:
                nonlocal result
                result += 1
            
            return node.val + descSum
        
        treeSum(root)
        return result