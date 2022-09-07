# 383. Ransom Note
"""
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}

        for n in ransomNote:
            letters[n] = letters.get(n, 0) + 1

        for m in magazine:
            if m in letters:
                if letters[m] > 0:
                    letters[m] -= 1
                    if letters[m] == 0:
                        del letters[m]
            if len(letters) == 0:
                return True

        return False
