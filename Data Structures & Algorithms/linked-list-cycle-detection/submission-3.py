# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # Tortoise & Hare
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next: # fast.next.next 하니까 nullpointer 방지
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False