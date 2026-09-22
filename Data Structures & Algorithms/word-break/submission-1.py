class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1]
        
        for i in range(len(s)):
            for j in memo:
                if s[j + 1 : i + 1] in wordDict:
                    memo.append(i)
                    break
        
        return memo[-1] == len(s) - 1