# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level_leftmost = root
        
        queue = deque()
        queue.append(root)
        while queue:
            next_queue = deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if next_queue:
                level_leftmost = next_queue[0]
            queue = next_queue
            
        return level_leftmost.val
        