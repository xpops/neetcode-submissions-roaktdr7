# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 한 층당 맨 오른쪽 노드 하나씩만 선택됨
        # root.right가 있으면 오른쪽으로, curDepth 가져가고 out에다가 [cur, curDepth] 튜플로 저장
        out = []
        self.helper(root, out, 0)
        return [node.val for node, depth in out]

    def helper(self, cur, out, curDepth) -> void:
        if not cur:
            return

        if not out or curDepth > out[-1][1]:
            out.append((cur, curDepth))
        
        nextDepth = curDepth + 1

        self.helper(cur.right, out, nextDepth)
        self.helper(cur.left, out, nextDepth)

        return