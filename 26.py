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

    def removeDuplicates_2Pointers(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l

    # Runtime: 172 ms
    # Memory: 15.5 MB


    def remove_duplicates(nums):
      # index of the next non-duplicate element
      count = 1
      i = 0
      while i < len(nums):
        if nums[count - 1] != nums[i]:
          nums[count] = nums[i]
          count += 1
        i += 1

      return count

      # Runtime: 94 ms
      # Memory: 15.7 MB
