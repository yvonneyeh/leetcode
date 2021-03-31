# 125. Valid Palindrome
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()   #Converts string to lower
        x = ''
        for i in s:
            if i.isalnum():   # Checks if string is alphanumeric
                x+=(i)
        return x==x[::-1]
