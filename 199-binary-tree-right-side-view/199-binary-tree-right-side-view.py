# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        NEW_LEVEL = '-'
        right_view = []
        
        queue = deque()
        queue.append(root)
        queue.append(NEW_LEVEL)
        
        while len(queue):
            node = queue.popleft()
            
            if node == NEW_LEVEL:
                len(queue) and queue.append(NEW_LEVEL)
                right_view.append(rightmost.val)
            else:
                rightmost = node
                node.left and queue.append(node.left)
                node.right and queue.append(node.right)
        
        return right_view