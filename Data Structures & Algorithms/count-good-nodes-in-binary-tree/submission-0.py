# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        dummy = TreeNode()
        self.h(root, root.val, dummy)
        return dummy.val
    
    def h(self, root, curMax, count: TreeNode) -> int:
        if not root:
            return

        if root.val >= curMax:
            count.val = count.val + 1
            curMax = root.val
        
        self.h(root.left, curMax, count)
        self.h(root.right, curMax, count)