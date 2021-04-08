# 1684. Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        # 1. counter of words that match
        # 2. look at every word in list
        # 3. check if characters match allowed word

        count = 0
        set_words = set(allowed)

        for word in words:
            if all(letter in set_words for letter in word):
                count += 1

        return count

# Runtime: 260 ms, faster than 38.29% of Python3 online submissions for Count the Number of Consistent Strings.
# Memory Usage: 16.1 MB, less than 42.51% of Python3 online submissions for Count the Number of Consistent Strings.
