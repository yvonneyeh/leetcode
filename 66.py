# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        while n >= 0:
            if digits[n]<9:
                digits[n] += 1
                return digits
            digits[n] = 0
            n -= 1
        return [1] + digits
    
# Runtime: 51 ms, faster than 36.82% of Python3 online submissions for Plus One.
# Memory Usage: 13.8 MB, less than 57.18% of Python3 online submissions for Plus One.