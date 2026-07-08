class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        curSum = [0]

        def dfs(i):
            if curSum[0] >= target or i >= len(nums):
                if curSum[0] == target:
                    res.append(subset.copy())
                return
            
            subset.append(nums[i])
            curSum[0] += nums[i]
            dfs(i)

            subset.pop()
            curSum[0] -= nums[i]
            dfs(i + 1)

        dfs(0)
        return res