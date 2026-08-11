class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sorting
        # 1의자리 수만 봤을 때 0, 1, 0, 1 alternate되는데
        # 중간에 이전거랑 같은 digit (0 다음에 또 0 or 1 다음에 또 1) 나오면 그 숫자가 없는거.

        nums.sort()
        prev = 1

        for i in range(len(nums)):
            cur = nums[i] % 2
            if cur == prev:
                return nums[i] - 1
            prev = cur
        
        return nums[-1] + 1