# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        dummy = TreeNode(1)
        self.heightHelper(root, dummy)
        return True if dummy.val == 1 else False
    
    def heightHelper(self, root, dummy) -> int:
        # base
        if not root:
            return -1
        
        if abs(self.heightHelper(root.left, dummy) - self.heightHelper(root.right, dummy)) > 1:
            dummy.val = 0
        
        return 1 + max(self.heightHelper(root.left, dummy), self.heightHelper(root.right, dummy))