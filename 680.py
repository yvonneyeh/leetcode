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

class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True

        r = len(s) - 1

        for l in range(len(s) // 2):

            if s[l] != s[r]:

                s1 = s[:l] + s[l+1:]
                s2 = s[:r] + s[r+1:]

                print(s[:l], s[l+1:])
                print(s[:r], s[r+1:])

                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                break

            r -= 1
        return False

class Solution:
    def validPalindrome(self, s: str) -> bool:
        h, t = 0, len(s) - 1  # head and tail
        while h < t:
            if s[h] != s[t]:  # delete s[h] or s[t] and validate palindrome finally
                 return s[h:t] == s[h:t][::-1] or s[h + 1:t + 1] == s[h + 1:t + 1][::-1]
            h, t = h + 1, t - 1
        return True
