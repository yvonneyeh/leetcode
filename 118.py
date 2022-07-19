# 118. Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1, n+1)]   # initialize triangle with all 1
        for i in range(1, n):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1] # update each as sum of two elements from above row
        return ans

# Dynamic Programming - Iterative
# Time Complexity : O(n^2)
# Space Complexity : O(n^2)
