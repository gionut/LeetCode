class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        see_ahead = node.next
        node.val = see_ahead.val
        node.next = see_ahead.next
        