class Solution: # using defaultdict: O(n) space
    def findDuplicate(self, nums: List[int]) -> int:
        checkDup = defaultdict(int)
        for num in nums:
            if checkDup[num]:
                return num
            else:
                checkDup[num] = 1