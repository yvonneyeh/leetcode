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

class Solution_ConstantMemory:
    def findDuplicates1(self, nums: List[int]) -> List[int]:
        result = []

        for i, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1

        return result

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                result.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return result

    # if all numbers appear once, they will map to corresponding index only once.
    # if we take negative of the number at the corresponding index,
    # by the end, the elements in the array will all become negative, provided that all numbers appear only once.
    # however, if a number appears twice, by the second time we want to take negative of the number at its corresponding index, we will find that it is already negative. hence, we can append it to our res.
    # since we are changing the original element in the array while traversing the array, we take the original positive number by taking abs().
