# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # root는 무조건.
        # 1) p, q가 root보다 작음: root.left에서 recurse
        # 2) p, q가 root보다 큼: root.right에서 recurse
        # 3) p는 root보다 작거나 같고 q는 root보다 큼 or p는 root보다 작고 q는 root보다 같거나 큼: return root (끝)

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root