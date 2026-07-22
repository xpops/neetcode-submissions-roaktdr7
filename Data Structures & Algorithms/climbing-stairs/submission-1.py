class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 1
        if n == 1:
            return 1
        
        prev = 1
        prevPrev = 1

        for i in range(2, n + 1):
            res = prev + prevPrev

            prevPrev = prev
            prev = res
        
        return res