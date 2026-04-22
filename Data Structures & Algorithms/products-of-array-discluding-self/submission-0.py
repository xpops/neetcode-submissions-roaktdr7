class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroIndex = i
                zeroCount += 1
            total_product *= nums[i]
        
        out = []
        # one zero
        if zeroCount == 1:
            product_except_zero = 1
            for i in range(len(nums)):
                if i == zeroIndex:
                    continue
                else:
                    product_except_zero *= nums[i]
            for num in nums:
                if num == 0:
                    out.append(product_except_zero)
                else:
                    out.append(int(total_product / num))

        # 0 or 2+ zero(es)
        else:
            for num in nums:
                if num == 0:
                    out.append(0)
                else:
                    out.append(int(total_product / num))

        return out