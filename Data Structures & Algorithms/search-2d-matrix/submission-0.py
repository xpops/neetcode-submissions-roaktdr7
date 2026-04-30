class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 먼저 어떤 row에 있는지 확인하고 그 안에서 binary search?
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = int((l + r) / 2)
            if matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                return True
        
        # loop이 끝났을 때 무조건 r 위치에 있게 됨.
        row = r
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = int((l + r) / 2)
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        
        return False