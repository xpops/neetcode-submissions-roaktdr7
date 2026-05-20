# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        digit = 1

        dummy = ListNode()
        prev = dummy

        over = 0
        while cur1 and cur2:
            digitSum = cur1.val + cur2.val + over
            over = 0
            if digitSum > 9:
                over = 1
                digitSum -= 10
            prev.next = ListNode(digitSum)
            prev = prev.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1:
            digitSum = cur1.val + over
            over = 0
            if digitSum > 9:
                over = 1
                digitSum -= 10
            prev.next = ListNode(digitSum)
            prev = prev.next
            cur1 = cur1.next
        
        while cur2:
            digitSum = cur2.val + over
            over = 0
            if digitSum > 9:
                digitSum -= 10
                over = 1
            prev.next = ListNode(digitSum)
            prev = prev.next
            cur2 = cur2.next
        
        if over:
            prev.next = ListNode(over)
        
        return dummy.next