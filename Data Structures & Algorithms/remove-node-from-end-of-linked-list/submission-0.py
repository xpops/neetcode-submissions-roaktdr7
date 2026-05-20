# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # iterate to find size
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        # when removing the head, move head and return
        if size == n:
            head = head.next
            return head

        # iterate size - n time to locate the node
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for i in range(size - n):
            prev = prev.next
        
        # remove node
        prev.next = prev.next.next
        return head
