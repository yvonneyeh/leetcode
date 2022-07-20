# 792. Number of Matching Subsequences
# Medium

# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans, mappings = 0, defaultdict(list)
        for index, char in enumerate(s):
            mappings[char].append(index)
        for word in words:
            prev, found = -1, True
            for c in word:
                tmp = bisect.bisect(mappings[c], prev)
                if tmp == len(mappings[c]):
                    found = False
                    break
                else: prev = mappings[c][tmp]
            ans += found == True
        return ans
