class Solution: # Keep track of curMax, curMin (cur를 포함하는 subarray product의 최대, 최소)
    def maxProduct(self, nums: List[int]) -> int:
        prevMax, prevMin = nums[0], nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            curMax = max(n, prevMax * n, prevMin * n)
            curMin = min(n, prevMax * n, prevMin * n)
            
            if curMax > res:
                res = curMax
            
            prevMax = curMax
            prevMin = curMin
        
        return res
