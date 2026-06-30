# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # without using dummy node
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, curMax):
            if not root:
                return 0

            res = 0
            if root.val >= curMax:
                curMax = root.val
                res = 1
            
            return res + dfs(root.left, curMax) + dfs(root.right, curMax)
        
        return dfs(root, root.val)