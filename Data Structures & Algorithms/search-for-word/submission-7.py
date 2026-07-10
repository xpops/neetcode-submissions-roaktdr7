class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        
        def dfs(i, j, w):
            # reached the end
            if w == len(word):
                return True
            # no match
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[w] or (i, j) in path:
                return False
            
            # if char matches
            path.add((i, j))
            res = dfs(i - 1, j, w + 1) or dfs(i, j + 1, w + 1) or dfs(i + 1, j, w + 1) or dfs(i, j - 1, w + 1)
            path.remove((i, j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        
        return False