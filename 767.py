# 767. Reorganize String
"""
Medium

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters."""

class Solution:
    def reorganizeString(self, s: str) -> str:

        n = len(s)
        dictionary = Counter(s)
        sorted_dict = dict(sorted(dictionary.items(),key=lambda x: x[1],reverse=True))

        for c in dictionary:
            if dictionary[c]>((n+1)//2):
                return ""

        result = [""] * n
        j = n
        while j > 0:
            i = 0
            while result[i] != "":  # find the start of empty slot.
                i+=1

            for letter in sorted_dict:  # Most frequent key will come first.
                while i < n and dictionary[letter]>0:
                    result[i] = letter
                    dictionary[letter] -= 1
                    i += 2
                    j -= 1

        return ''.join(result)
