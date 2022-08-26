# 344. Reverse String
# Easy
# Write a function that reverses a string. The input string is given as an array of characters s.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

# Runtime: 192 ms, faster than 75.12% of Python3 online submissions for Reverse String.
# Memory Usage: 18.7 MB, less than 52.05% of Python3 online submissions for Reverse String.

    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

        # O(n) time
        # O(1) space
