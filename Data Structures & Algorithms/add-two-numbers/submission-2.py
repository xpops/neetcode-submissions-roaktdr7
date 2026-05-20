# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # initialize
        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        prev = dummy

        # loop through the end
        over = 0
        while cur1 or cur2 or over:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0

            # add & handle carryover
            digitSum = v1 + v2 + over
            over = 0
            if digitSum > 9:
                over = 1
                digitSum -= 10
            prev.next = ListNode(digitSum)

            # update ptrs
            prev = prev.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        
        return dummy.next