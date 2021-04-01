# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        while count < len(nums)-1:
            if nums[count] == nums[count+1]:
                nums.pop(count)
            else:
                count += 1

# Runtime: 96 ms, faster than 38.19% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 16 MB, less than 52.79% of Python3 online submissions for Remove Duplicates from Sorted Array.
