class Solution:
    def rob(self, nums: List[int]) -> int:
        inclFirst, inclLast = 0, 0
        
        def helper(nums):
            prev2, prev1 = 0, 0
            for n in nums:
                cur = max(prev2 + n, prev1)
                prev2 = prev1
                prev1 = cur
            return prev1
        
        # if len(nums) == 1:
        #     return nums[0]

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))