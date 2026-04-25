class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 일단 sorting은 하면 안됨. 순서가 상관있기때문에
        l = 0
        r = len(heights) - 1
        max = 0

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            if curr_area > max:
                max = curr_area
            if heights[l] > heights[r]:
                r -= 1
                continue
            else:
                l += 1
                continue
        
        return max