# 202. Happy Number
"""
Easy

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def find_square_sum(num):
            _sum = 0
            while (num > 0):
                digit = num % 10
                _sum += digit * digit
                num //= 10
            return _sum

        slow, fast = n, n
        while True:
            slow = find_square_sum(slow)  # move one step
            fast = find_square_sum(find_square_sum(fast))  # move two steps
            if slow == fast:  # found the cycle
              break
        return slow == 1  # see if the cycle is stuck on the number '1'



class SetSolution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)
            n = self.sumSquareDigits(n)

            if n == 1:
                return True

        return False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
