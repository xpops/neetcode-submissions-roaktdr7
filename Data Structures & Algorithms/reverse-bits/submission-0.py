class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        cur = 1
        for i in range(32):
            if n & cur != 0:
                res |= 1 << 31 - i
            cur = cur << 1
        
        return res