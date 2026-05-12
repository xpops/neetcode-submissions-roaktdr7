class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # determine m in left or right
        # if left:
        #   if target < mid:
        #       if target < left:
        #           search right
        #       else:
        #           search left
        #   if target > mid:
        #       search right
        # if right:
        #   if target < mid:
        #       search left
        #   if target > mid:
        #       search right

        l, r = 0, len(nums) - 1

        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]: # left
                if target < nums[m]:
                    if target < nums[l]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    l = m + 1
            
            else: #right
                if target > nums[m]:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    r = m - 1
        
        return -1