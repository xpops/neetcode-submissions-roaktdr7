class Solution: # 1. Sorting: O(nlogn)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        # sort by start
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] > prev[1]: # no overlap
                res.append(prev)
                prev = cur
            else: # overlap
                prev = [prev[0], max(cur[1], prev[1])]
        
        res.append(prev) # 마지막에 남은거 넣어주기
    
        return res
