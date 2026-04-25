class Solution: # Sorting
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        while nums: # nums[i]와 같은애들을 다 없애도 되나? 얘가 들어가는 triplet은 다 나온거잖아.
            target = 0 - nums[0]
            j = 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    # 중복인지 확인. short circuit으로 인덱스부터 확인해서 IndexOutOfBounds 방지
                    if j == 1 or k == len(nums) - 1 or nums[j] != nums[max(j - 1, 1)] or nums[k] != nums[min(k + 1, len(nums) - 1)]:
                        out.append([nums[0], nums[j], nums[k]])
                    k -= 1
                    j += 1
            nums = [x for x in nums if x != nums[0]]
        return out