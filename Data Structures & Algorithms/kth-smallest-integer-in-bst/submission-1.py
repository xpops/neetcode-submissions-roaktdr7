# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # inorder traversal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrder(root, k, arr):
            if not root or len(arr) == k: # early termination
                return
            
            inOrder(root.left, k, arr)
            arr.append(root.val)
            inOrder(root.right, k, arr)
            
            return
        
        arr = []
        inOrder(root, k, arr)
        return arr[k - 1]