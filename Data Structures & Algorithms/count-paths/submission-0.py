class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        up = [[0 for x in range(n)] for y in range(m)]

        # up[m, n] = up[m - 1, n] + up[m, n - 1]
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    up[i][j] = 1
                    continue
                up[i][j] = up[max(0, i - 1)][j] + up[i][max(0, j - 1)]

        return up[m - 1][n - 1]