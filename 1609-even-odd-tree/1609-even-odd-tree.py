# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        if root.val % 2 == 0:
            return False
        
        queue = deque()
        queue.append(root)
        while queue:
            next_queue = deque()
            prev_node = None
            while queue:
                node = queue.popleft()
            
                if level % 2 == 0: # if even
                    if node.val % 2 == 0: # should have odd values
                        return False
                    if prev_node and prev_node.val >= node.val: # should be increasing
                        return False
                else: # if odd
                    if node.val % 2 == 1: # should have even values
                        return False
                    if prev_node and prev_node.val <= node.val: # should be decreasing
                        return False
                prev_node = node
                
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            
            queue = next_queue
            level += 1
            
        return True