#1816. Truncate Sentence

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # split string by the spaces
        # add all the words to a list
        # return words from index 0 to range K
        # separated words with new spaces

        words = s.split()
        # print(words)

        return " ".join(words[0:k])

# Runtime: 28 ms, faster than 86.25% of Python3 online submissions for Truncate Sentence.
# Memory Usage: 14.4 MB, less than 23.22% of Python3 online submissions for Truncate Sentence.
