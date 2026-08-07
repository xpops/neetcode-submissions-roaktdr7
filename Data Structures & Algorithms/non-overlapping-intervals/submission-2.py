class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start then end
        intervals.sort(key=lambda i : (i[1]))
        
        res = 0
        prev = intervals[0]
        curNum = 0
        for cur in intervals[1:]:
            if prev[1] <= cur[0]:
                res += curNum
                curNum = 0
                prev = cur
            else:
                curNum += 1

        res += curNum
        return res