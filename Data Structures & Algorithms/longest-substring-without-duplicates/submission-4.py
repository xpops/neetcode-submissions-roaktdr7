class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        curSet = set()

        while r < len(s):
            cur = s[r]
            if cur in curSet: # 중복
                while s[l] != cur:
                    curSet.remove(s[l])
                    l += 1
                curSet.remove(s[l])
                l += 1
            else: # 중복없음
                curSet.add(cur)
                longest = max(longest, r - l + 1)
                r += 1
    
        return longest
