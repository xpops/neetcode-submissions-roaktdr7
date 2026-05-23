class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        
        while True:
            s = nums[s] # move 1
            f = nums[nums[f]] # move 2
            if s == f:
                break
        
        i, j = 0, s
        while i != j:
            i = nums[i]
            j = nums[j]
        
        return i