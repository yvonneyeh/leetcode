# 17. Letter Combinations of a Phone Number - Backtracking
# Letter Combinations of a Phone Number
# Medium

# You are given a string digits made up of digits from 2 through 9 inclusive.

# Each digit (not including 1) is mapped to a set of characters as shown below:

# A digit could represent any one of the characters it maps to.

# Return all possible letter combinations that digits could represent. You may return the answer in any order.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(i, current_string):
            if len(current_string) == len(digits):
                result.append(current_string)
                return
            for character in dictionary[digits[i]]:
                backtrack(i + 1, current_string + character)

        if digits:
            backtrack(0, "")

        return result
