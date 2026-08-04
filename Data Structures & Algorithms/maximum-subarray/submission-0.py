class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        resMax = nums[0]
        
        for n in nums[1:]:
            cur = max(n, prev + n)
            if cur > resMax:
                resMax = cur
            prev = cur

        return resMax