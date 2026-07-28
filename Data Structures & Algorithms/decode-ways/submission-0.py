class Solution:
    def numDecodings(self, s: str) -> int:

        if int(s[0]) == 0:
            return 0

        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            lastChar = int(s[max(i - 1, 0)])
            c = int(s[i])

            if lastChar == 1:
                if c == 0:
                    cur = prev2
                else:
                    cur = prev2 + prev1

            elif lastChar == 2:
                if c == 0:
                    cur = prev2
                elif c > 6:
                    cur = prev1
                else:
                    cur = prev2 + prev1
            
            else:
                if c == 0:
                    return 0
                cur = prev1
            
            prev2 = prev1
            prev1 = cur
        
        return prev1
