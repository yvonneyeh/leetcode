# 1470. Shuffle the Array
# Easy

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res

# Runtime: 60 ms, faster than 62.02% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.6 MB, less than 17.61% of Python3 online submissions for Shuffle the Array.
