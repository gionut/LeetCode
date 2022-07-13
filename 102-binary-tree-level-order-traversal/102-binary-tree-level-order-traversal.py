# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        traversal = []
        
        while len(stack):
            nodes = stack
            stack = []
            traversal.append([])
            for node in nodes:
                traversal[-1].append(node.val)
                node.left and stack.append(node.left)
                node.right and stack.append(node.right)
                
        return traversal
                