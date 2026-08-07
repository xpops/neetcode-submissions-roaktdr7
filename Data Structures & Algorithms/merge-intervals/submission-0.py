class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        # sort by start
        intervals.sort(key=lambda x: x[0])

        new = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] > new[1]: # no overlap
                res.append(new)
                new = cur
            else: # overlap
                new = [new[0], max(cur[1], new[1])]
        
        res.append(new)
    
        return res
