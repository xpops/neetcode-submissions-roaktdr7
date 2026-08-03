class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [0 for num in nums]

        for i in range(len(nums) - 1, -1, -1):
            curMax = 1            
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    curMax = max(curMax, 1 + lis[j])
            lis[i] = curMax
        
        return max(lis)