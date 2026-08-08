"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()

        count = 0
        maxCount = count
        i, j = 0, 0
        while i < len(starts) and j < len(ends):
            if starts[i] < ends[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1

            maxCount = max(count, maxCount)
        
        return maxCount