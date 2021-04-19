#387. First Unique Character in a String

# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:

        d = {}

        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1

# Runtime: 132 ms, faster than 47.56% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.4 MB, less than 68.46% of Python3 online submissions for First Unique Character in a String.
