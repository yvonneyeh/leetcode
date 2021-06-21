# 1528. Shuffle String
# Easy
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)

    # Runtime: 48 ms, faster than 94.54% of Python3 online submissions for Shuffle String.
    # Memory Usage: 14 MB, less than 91.99% of Python3 online submissions for Shuffle String.

    def restoreString_sortedzip(self, s: str, indices: List[int]) -> str:
        return "".join(c for _, c in sorted(zip(indices, s)))

    # Runtime: 56 ms, faster than 59.20% of Python3 online submissions for Shuffle String.
    # Memory Usage: 14.4 MB, less than 18.54% of Python3 online submissions for Shuffle String.
