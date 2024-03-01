# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        val_map = {}
        for node in nodes:
            val_map[node.val] = node
        # if len(nodes) == 1:
        #     return nodes[0]
        
        result = None
        def dfs(node):
            # print(node.val)
            if not node:
                return False
            
            nonlocal result
            if node.val in val_map:
                result = node
                return True
            
            contains_left = False
            contains_right = False
            if node.left:
                contains_left = dfs(node.left)
            if node.right:
                contains_right = dfs(node.right)
            
            if contains_left and contains_right:
                result = node
            
        dfs(root)
        return result
                    