class Solution:
    def countBits(self, n: int) -> List[int]:
        cur = 0
        res = [0]
        for i in range(n):
            num = i
            while num % 2 != 0: # until first 0 is encountered
                cur -= 1
                num = math.floor(num / 2)
            cur += 1
            res.append(cur)
        
        return res
