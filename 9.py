# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]

# Runtime: 113 ms, faster than 24.83% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.8 MB, less than 58.29% of Python3 online submissions for Palindrome Number.

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        inputNum = x
        newNum = 0
        while x > 0:
            newNum = newNum * 10 + x % 10
            x = x//10
        return newNum == inputNum
