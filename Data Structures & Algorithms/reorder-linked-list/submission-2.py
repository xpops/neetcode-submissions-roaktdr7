# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # Reverse and Merge (slow and fast ptr to find mid)
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1 iteration to find mid
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # .5 iteration to reverse mid
        prev, curr = None, mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        # reorder
        curr1, curr2 = head, head2
        while curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2