class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        pivot = 0
        
        # find pivot
        while l <= r:
            if nums[l] < nums[r]: # does not contain pivot
                pivot = l

            m = int((l + r) / 2)

            if nums[m - 1] > nums[m]:
                pivot = m

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        if pivot == 0:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target:
            l, r = 0, pivot - 1
        else:
            l, r = pivot, len(nums) - 1
        
        while l <= r:
            m = int((l + r) / 2)
            
            if target == nums[m]:
                return m
            
            elif target < nums[m]:
                r = m - 1

            else:
                l = m + 1
        
        return -1