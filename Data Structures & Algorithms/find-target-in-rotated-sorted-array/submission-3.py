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
                break

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        # set l, r for binary search
        if pivot == 0: # unshifted array
            l, r = 0, len(nums) - 1
        elif nums[0] <= target: # target in left(big) portion
            l, r = 0, pivot - 1
        else: # target in right(small) portion
            l, r = pivot, len(nums) - 1
        
        # simple binary search
        while l <= r:
            m = int((l + r) / 2)
            
            if target == nums[m]:
                return m
            
            elif target < nums[m]:
                r = m - 1

            else:
                l = m + 1
        
        return -1