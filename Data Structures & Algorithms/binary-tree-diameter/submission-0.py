# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dummy = TreeNode()
        self.diameterHelper(root, dummy)
        return dummy.val
    
    # returns longest path that passes through the root
    def diameterHelper(self, root: Optional[TreeNode], dummy: TreeNode) -> int:
        # base case
        if root == None:
            return -1
        
        curDiameter = self.diameterHelper(root.left, dummy) + 1 + self.diameterHelper(root.right, dummy) + 1
        dummy.val = max(curDiameter, dummy.val)
        curHeight = max(self.diameterHelper(root.left, dummy), self.diameterHelper(root.right, dummy)) + 1

        return curHeight