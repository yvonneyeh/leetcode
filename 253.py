# 253 · Meeting Rooms II
# LintCode 919
"""
Medium

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

(0,8),(8,10) is not conflict at 8

Example 1
    Input: intervals = [(0,30),(5,10),(15,20)]
    Output: 2
    Explanation:
    We need two meeting rooms
    room1: (0,30)
    room2: (5,10),(15,20)
Example 2
    Input: intervals = [(2,7)]
    Output: 1
    Explanation: Only need one meeting room

"""


from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:

        start = sort([i.start for i in intervals])
        end = sort([i.end for i in intervals])

        room_count, max_rooms = 0, 0
        a, b = 0, 0 # 2 pointers

        while a < len(intervals):
            if end[a] > start[b]:
                a += 1
                room_count += 1
            else:
                # end[a] < start[b] or end[a] == start[b]
                b += 1
                room_count -= 1
            max_rooms = max(room_count, max_rooms)

        return max_rooms

    # Time: O(n log n)
    # Memory: O(n)
