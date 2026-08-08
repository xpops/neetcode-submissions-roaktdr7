"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not len(intervals):
            return True

        intervals.sort(key=lambda i : i.start)

        prev = intervals[0]
        for interval in intervals[1:]:
            if interval.start < prev.end:
                return False
            prev = interval
        
        return True