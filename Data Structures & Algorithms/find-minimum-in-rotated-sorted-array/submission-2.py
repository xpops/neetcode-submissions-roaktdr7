class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        l, r = 0, int(len(nums) / 2)
        prev = r

        while r > -1 and l <= r:
            m = int((l + r) / 2)

            if nums[m - 1] > nums[m]:
                return nums[m]
            
            if nums[m] > nums[prev]:
                l = m + 1
            else:
                r = m - 1
            
            prev = m
        
        l, r = int(len(nums) / 2), len(nums) - 1
        prev = l
        
        while l < len(nums) and l <= r:
            m = int((l + r) / 2)

            if nums[m - 1] > nums[m]:
                return nums[m]
            
            if nums[m] < nums[prev]:
                r = m - 1
            else:
                l = m + 1
            
            prev = m