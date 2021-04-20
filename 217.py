# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(nums) != len(set(nums))

# Runtime: 116 ms, faster than 76.03% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 20.1 MB, less than 80.27% of Python3 online submissions for Contains Duplicate.
