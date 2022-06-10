#27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start
    
# Runtime: 73 ms, faster than 5.41% of Python3 online submissions for Remove Element.
# Memory Usage: 13.8 MB, less than 61.56% of Python3 online submissions for Remove Element.