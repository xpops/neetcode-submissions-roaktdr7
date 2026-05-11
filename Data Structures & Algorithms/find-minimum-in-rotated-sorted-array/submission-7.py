class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]

            m = int((l + r) / 2)

            if nums[m - 1] > nums[m]:
                return nums[m]

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1


