# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(n):
            queue = deque()
            queue.append(n)
            
            traversal = []
            while queue:
                n = queue.popleft()
                traversal.append(n.val if n else None)
                if n:
                    queue.append(n.left if n.left else None)
                    queue.append(n.right if n.right else None)

            return traversal
        
        if p == None and q == None:
            return True
        if p == None or q is None:
            return False
        
        traversal_p = bfs(p)
        traversal_q = bfs(q)
        
        return traversal_p == traversal_q