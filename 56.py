# 56. Merge Intervals
"""
Medium
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
         # Sort by start time
        sorted_intervals = sorted(intervals)

        # Initialize merged_intervals with the earliest interval
        merged_intervals = [sorted_intervals[0]]

        for current_interval_start, current_interval_end in sorted_intervals[1:]:
            last_merged_interval_start, last_merged_interval_end = merged_intervals[-1]

            # If the current interval overlaps with the last merged interval, use the
            # later end time of the two
            if (current_interval_start <= last_merged_interval_end):
                merged_intervals[-1] = (last_merged_interval_start,
                                       max(last_merged_interval_end,
                                           current_interval_end))
            else:
                # Add the current interval since it doesn't overlap
                merged_intervals.append((current_interval_start, current_interval_end))

        return merged_intervals


    def merge_refactored(self, intervals: List[List[int]]) -> List[List[int]]:
         # Sort by start time
        intervals.sort(key=lambda pair: pair[0])

        # Initialize merged_intervals with the earliest interval
        merged = [intervals[0]]

        for start, end in intervals:
            prev_start, prev_end = merged[-1]

            # If the current interval overlaps with the last merged interval, use the
            # later end time of the two
            if start <= prev_end:
                merged[-1] = (prev_start, max(prev_end, end))
            else:
                # Add the current interval since it doesn't overlap
                merged.append([start, end])

        return merged

    def merge_cleaned(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # merge
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


# Time: O(n log n)
