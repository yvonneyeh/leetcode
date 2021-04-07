# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

            wordlist = s.split()
            if wordlist:
                return len(wordlist[-1])
            return 0

#
# Runtime: 20 ms, faster than 98.96% of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.3 MB, less than 64.99% of Python3 online submissions for Length of Last Word.
