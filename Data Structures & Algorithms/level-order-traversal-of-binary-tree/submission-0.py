# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue 두개?
        q1, q2, cur, out = [], [], [], []

        if not root:
            return []

        q1.append(root)

        while q1 or q2:
            while q1:
                popped = q1.pop(0)
                if popped.left:
                    q2.append(popped.left)
                if popped.right:
                    q2.append(popped.right)
                cur.append(popped.val)
            if cur:
                out.append(cur)
            cur = []

            while q2:
                popped = q2.pop(0)
                if popped.left:
                    q1.append(popped.left)
                if popped.right:
                    q1.append(popped.right)
                cur.append(popped.val)
            if cur:
                out.append(cur)
            cur = []

        return out
        