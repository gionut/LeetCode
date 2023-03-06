class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        crt = node
        see_ahead = node.next
        while see_ahead.next:
            crt.val = see_ahead.val
            crt = crt.next
            see_ahead = see_ahead.next
        crt.val = see_ahead.val
        crt.next = None
        