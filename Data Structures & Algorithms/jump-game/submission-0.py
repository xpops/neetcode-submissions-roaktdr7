class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = len(nums) - 1
        
        while cur > 0:
            i = cur - 1
            while i >= 0:
                if cur - i <= nums[i]:
                    cur = i
                    break
                i -= 1
                if i < 0: # reached the start
                    return False
        
        return True
