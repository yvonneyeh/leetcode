# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        joined1 = "".join(word1)
        joined2 = "".join(word2)

        return joined1 == joined2

# Runtime: 28 ms, faster than 83.96% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Memory Usage: 14.3 MB, less than 62.27% of Python3 online submissions for Check If Two String Arrays are Equivalent.
