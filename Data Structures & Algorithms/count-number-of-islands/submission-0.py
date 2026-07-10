class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited:
                return False
            
            if grid[r][c] == "1":
                
                visited.add((r, c))

                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)

                return True
            
            return False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c):
                    res += 1
        
        return res