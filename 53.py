#53. Maximum Subarray

class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
    
# Runtime: 1266 ms, faster than 18.30% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.6 MB, less than 9.67% of Python3 online submissions for Maximum Subarray.