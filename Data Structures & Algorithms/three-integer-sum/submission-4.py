class Solution: # Sorting
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i, n in enumerate(nums): # enumerate(): index랑 value 둘다 킵할수있음
            if n > 0: # sorted이고, 우편만 보니까
                break

            if i > 0 and n == nums[i - 1]: # 중복들 다 건너뛰기 & short-circuit 이용
                continue

            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j - 1] and j < k: # 왼쪽만 같고 오른쪽 다르면 어차피 합이 달라서 append안됨. 그러므로 한쪽만 확인
                        j += 1
        return out