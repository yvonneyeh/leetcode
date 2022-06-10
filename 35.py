#35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
    
# Runtime: 61 ms, faster than 64.26% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.7 MB, less than 81.16% of Python3 online submissions for Search Insert Position.