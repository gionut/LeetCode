# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderIndex = {}
        for index, val in enumerate(inorder):
            self.inorderIndex[val] = index
        
        self.preorder = preorder
        
        return self.buildRecursive(0, len(inorder))
        
    def buildRecursive(self, left, right):
        if left < right:
            node = TreeNode()
            
            node.val = self.preorder.pop(0)
            
            rootIndex = self.inorderIndex[node.val]
            
            node.left = self.buildRecursive(left, rootIndex)
            node.right = self.buildRecursive(rootIndex+1, right)
            
            return node
        return None