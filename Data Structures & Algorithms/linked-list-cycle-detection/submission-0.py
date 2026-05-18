# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited로 마킹할 방법이 있나?
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
            if count > 1000:
                return True
        return False
            