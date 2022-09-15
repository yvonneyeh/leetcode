# 680. Valid Palindrome II
"""
Easy
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false


Constraints:
1 <= s.length <= 105
s consists of lowercase English letters."""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]: # check for standard palindrome
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]: # step through while chars match
                left += 1
                right -= 1
            else:
                s1 = s[left:right] # list slicing, removes right char
                s2 = s[left+1:right+1] # remove left char, include right
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True
