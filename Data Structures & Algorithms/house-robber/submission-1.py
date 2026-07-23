class Solution:
    def rob(self, nums: List[int]) -> int:

        prev2, prev1 = 0, 0

        # [prev2, prev1, n, n + 1, n + 2]
        for n in nums:
            cur = max(prev1, prev2 + n)
            prev2 = prev1
            prev1 = cur

        return cur