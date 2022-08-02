# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# notes
# can take 1 or 2 steps
# modulo?
# keep iterating through until n = 1 / n = 2
# recursion = base case = n = 1

# edge cases =
# n = 0
# n = 1
# n = 2

class Solution:
    @cache # without this,
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
