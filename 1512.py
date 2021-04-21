# 1512. Number of Good Pairs
# Easy

# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.




class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        pairs = {}
        total = 0

        for num in nums:
            if num in pairs:
                total += pairs[num]
                pairs[num] += 1
            else:
                pairs[num] = 1


        return total

# Runtime: 32 ms, faster than 74.35% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14.3 MB, less than 10.51% of Python3 online submissions for Number of Good Pairs.
