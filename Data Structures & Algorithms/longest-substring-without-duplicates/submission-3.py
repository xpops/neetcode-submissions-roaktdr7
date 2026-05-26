class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 1

        while r <= len(s): # 마지막 char가 longest에 포함될때를 대비하여 <= 사용
            subString = s[l : r]
            if len(list(subString)) == len(set(subString)): # no duplicates
                longest = max(longest, r - l)
            else:
                l += 1
                continue
            r += 1
        
        return longest
