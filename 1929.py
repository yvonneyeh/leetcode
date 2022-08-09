# 1929. Concatenation of Array

"""
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

==========

nums = [1,1]
ans = [1,1,1,1]

nums = [9, 8 , 7, 6]
ans = [9, 8 , 7, 6, 9, 8 , 7, 6]

concatenate array by adding `nums` to itself to make `ans`
ans = nums + nums

create a new ans array from nums
look at every item in the array
add item to index i + n to ans for each

enumerate -> index, value

runtime: 0(n)
space: O(2n)

qs
runtime of array concatenation?
2*nums

[1,1,1,1] ->  (1) * 4 ???

test cases:
empty nums or n > 1000 -> return empty array
if n[i] = 0 or >1000) -> return empty []
assume all items in array are ints
[8] -> [8,8]

"""


nums = [1,2,1]

def get_concatenation_pythonic(nums):
    return nums * 2

def getConcatenation(nums):
    ans = nums
    for num in nums:
    #     # if index >= 1 and index <= 1000 and value >= 1 and value <= 1000:
        # ans.append(num)
        print(num)
    #     # ans[index + len(nums)] = value
    #     # else:
    #     #     return []
    return ans
    # return nums * 2
