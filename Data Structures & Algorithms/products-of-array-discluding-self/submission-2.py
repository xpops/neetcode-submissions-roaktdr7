class Solution: # Prefix & Suffix
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j = len(nums)
        prefix = [1] * j
        suffix = [1] * j
        prefix[0] = nums[0]
        suffix[j - 1] = nums[j - 1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
            suffix[j - 1 - i] = suffix[j - i] * nums[j - 1 - i]
        
        out = []
        out.append(suffix[1])
        for i in range(1, j - 1):
            out.append(prefix[i - 1] * suffix[i + 1])
        out.append(prefix[j - 2])

        return out