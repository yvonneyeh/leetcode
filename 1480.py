# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:


        # create output list
        # loop through array, for range length of list
        # keep sum counter and add nums to Sum
        # append to new list


        output = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            output.append(total)

        return output

# Runtime: 64 ms, faster than 5.73% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.4 MB, less than 72.25% of Python3 online submissions for Running Sum of 1d Array.

class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        current = 0
        for num in nums:
            current += num
            result.append(current)

        return result
