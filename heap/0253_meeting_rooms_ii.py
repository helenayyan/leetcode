"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

"""
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        freerooms = []
        intervals.sort(key=lambda x: x[0])

        if not intervals:
            return 0

        heapq.heappush(freerooms, intervals[0][1])

        for interval in intervals[1:]:
            if freerooms[0] <= interval[0]:
                heapq.heappop(freerooms)
            heapq.heappush(freerooms, interval[1])

        return len(freerooms)
