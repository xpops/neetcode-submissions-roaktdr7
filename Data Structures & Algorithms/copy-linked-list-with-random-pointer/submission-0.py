"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {}

        # copy
        curr = head
        dummy = Node(0) # dummy node (new head)
        prevCopy = dummy
        while curr:
            currCopy = Node(curr.val)
            node_dict[curr] = currCopy # connect orig with copy (hashmap)
            prevCopy.next = currCopy
            prevCopy = currCopy
            curr = curr.next
        prevCopy.next = None # last elem

        # handle random
        curr = head
        while curr:
            if not curr.random:
                node_dict[curr].random = None
                curr = curr.next
                continue
            node_dict[curr].random = node_dict[curr.random]
            curr = curr.next
        
        return dummy.next