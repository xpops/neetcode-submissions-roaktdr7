class Solution: # using dict
    def findDuplicate(self, nums: List[int]) -> int:
        checkDup = {}
        for num in nums:
            if num in checkDup:
                return num
            else:
                checkDup[num] = 1