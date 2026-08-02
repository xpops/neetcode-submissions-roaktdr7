class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1]
        
        for i in range(len(s)):
            cur = False
            for j in memo:
                if s[j + 1 : i + 1] in wordDict:
                    cur = True
                    break
            
            if cur:
                memo.append(i)
        
        return memo[-1] == len(s) - 1