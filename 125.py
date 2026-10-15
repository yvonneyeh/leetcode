# 125. Valid Palindrome
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#
#         s = s.lower()   #Converts string to lower
#         x = ''
#         for i in s:
#             if i.isalnum():   # Checks if string is alphanumeric
#                 x+=(i)
#         return x==x[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(c): # checks if string is alphanumeric using ASCII values
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9')
                    )

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not is_alphanumeric(s[l]):
                l += 1
            while r > l and not is_alphanumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
