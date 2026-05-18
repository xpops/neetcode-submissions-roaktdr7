# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: # Reverse and Merge (1.5 iterations to find mid)
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 iteration to find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # .5 iteration to find mid
        midPrev = head
        for i in range(0, math.ceil(length / 2) - 1):
            midPrev = midPrev.next
        mid = midPrev.next
        midPrev.next = None

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
            temp = curr1.next
            curr1.next = curr2
            curr2 = curr2.next
            curr1.next.next = temp
            curr1 = temp