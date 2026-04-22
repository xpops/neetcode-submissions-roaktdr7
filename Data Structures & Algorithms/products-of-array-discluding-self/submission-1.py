class Solution: # Prefix & Suffix
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[len(nums) - 1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])
            suffix.append(suffix[i - 1] * nums[len(nums) - 1 - i])
        
        out = []
        out.append(suffix[len(nums) - 2])
        for i in range(1, len(nums) - 1):
            out.append(prefix[i - 1] * suffix[len(nums) - 2 - i])
        out.append(prefix[len(nums) - 2])

        return out