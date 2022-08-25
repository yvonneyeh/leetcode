# 252. Meeting Rooms
# LintCode 920
"""
Easy

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Example 1

    Input: intervals = [(0,30),(5,10),(15,20)]
    Output: false

    Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict

Example 2

    Input: intervals = [(5,8),(9,15)]
    Output: true
    Explanation: Two times will not conflict
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
    @return: if a person could attend all meetings
    """

    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True
