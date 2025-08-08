# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move `prev` to the node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Start reversing from `start`
        start = prev.next  # First node to reverse
        then = start.next  # Node that will be moved

        # Step 3: Reverse sublist from left to right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next
