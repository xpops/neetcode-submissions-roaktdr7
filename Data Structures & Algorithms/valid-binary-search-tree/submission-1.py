# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, least, most):
            # base case
            if not root:
                return True
            
            if root.val > least and root.val < most:
                return helper(root.left, least, root.val) and helper(root.right, root.val, most)
            
            return False

        return helper(root, -math.inf, math.inf)