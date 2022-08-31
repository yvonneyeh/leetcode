# 55. Jump Game
"""
Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy algo - work backwards
        # see if there is a -1 jump that can reach
        # set max pointer to last item in list
        # loop through the list backwards, checking if it possible to reach the pointer
        # if the number is greater than the goal it means we can reach it

        target = len(nums) - 1

        # start, stop, step
        for i in range(len(nums) - 2, -1 , -1 ):
            print("target", target)
            print("i", i)
            if i + nums[i] >= target:
                print("i + nums[i]", i + nums[i])
                target = i

        return target == 0
