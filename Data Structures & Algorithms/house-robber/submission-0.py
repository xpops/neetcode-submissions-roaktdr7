class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        cur = 0

        for n in range(2, len(nums)):
            cur = max(prev1, prev2 + nums[n])
            prev2 = prev1
            prev1 = cur

        return cur
