#1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):

        # create dictionary to keep track of what we have seen
        # loop through the list
        # enumerate items
        # subtract current num from target value and add to dict as key
        # if num exists in dictionary, return index of dict value

        seen = {}

        for i, value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return [seen[difference], i]
            seen[value] = i
        return []
