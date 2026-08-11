class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """ XOR
        같은 숫자 두개를 XOR하면 0.
        nums의 숫자와 실제 모든 숫자 (nums + res)
        """

        res = 0
        for n in nums:
            res ^= n
        for n in range(len(nums) + 1):
            res ^= n
        
        return res
