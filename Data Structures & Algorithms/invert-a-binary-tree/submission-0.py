# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeHelper(root)
    
    def invertTreeHelper(self, cur: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if cur == None:
            return

        # switch
        temp = cur.left
        cur.left = cur.right
        cur.right = temp

        # recurse
        self.invertTreeHelper(cur.left)
        self.invertTreeHelper(cur.right)

        return cur