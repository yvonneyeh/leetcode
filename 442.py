# 442. Find All Duplicates in an Array
# Medium
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        dict = {}
        lst = []

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1

        for key, value in dict.items():
            if value == 2:
                lst.append(key)

        return lst

# Runtime: 352 ms, faster than 68.67% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 22.6 MB, less than 30.49% of Python3 online submissions for Find All Duplicates in an Array.
