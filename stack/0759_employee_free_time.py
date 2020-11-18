"""
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.


"""
# Definition for an Interval.
from collections import deque


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        stack = deque()
        stack.append(float('-inf'))
        res = []
        intervals = []
        for events in schedule:
            for interval in events:
                intervals.append([interval.start, interval.end])

        intervals = sorted(intervals, key=lambda x: x[0])

        for interval in intervals:
            if interval[0] > stack[-1]:
                res.append(Interval(stack[-1], interval[0]))
                stack.append(interval[1])
            else:
                if interval[1] >= stack[-1]:
                    stack.append(interval[1])
        return res[1:]
