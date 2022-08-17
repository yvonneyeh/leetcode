# 523. Continuous Subarray Sum
"""
Medium

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

# create window with 2 items
# sum 2 items
# if sum = k, return true
# if false, slide window forward, repeat
# return false
        #
        # left = 0
        # current_sum = 0
        # for right in range(1, len(nums)):
        #     current_sum = nums[left] + nums[right]
        #     print(current_sum)
        #
        #         if current_sum % k == 0:
        #             return True
        #         else:
        #             left += 1
        # return False

        # wrong solution, I didn't understand the problem initally >_<

# create dict with key = num, value = remainder
# if we encounter the same remainder it means we added a sum that equals a multiple of k

        current_sum = 0
        remainders = {0:-1}
        for i, num in enumerate(nums):
            current_sum = current_sum + num
            remainder = current_sum % k
            if remainder not in remainders:
                remainders[remainder] = i
            elif (remainder in remainders) and (i - remainders[remainder]>=2) :
                # ((i - (remainders[remainder]+1) + 1 )>=2)
                return True

        return False
