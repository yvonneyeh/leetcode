#1832. Check if the Sentence Is Pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        return len(set(sentence)) == 26


# Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Check if the Sentence Is Pangram.
