# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        # Purpose: to reverse a int.

        # init. result and symbol
        res = 0
        sym = 1

        # neg. cases
        if x < 0:
            # symbol to -1
            sym = -1
            # value to positive
            x *= -1

        while x:
            # find remainder
            rem = x % 10
            # add up to result
            res = res * 10 + rem
            # check former digit
            x = int(x/10)

        # return result
        if res >= pow(2, 31):
            return 0
        else:
            return res * sym

# Runtime: 32 ms, faster than 66.80% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14.3 MB, less than 46.03% of Python3 online submissions for Reverse Integer.
