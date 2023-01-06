# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True

        return False

# Runtime 109 ms Beats 33.79%
# Memory 15.2 MB Beats 11.45%

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:

        # if length of both words are not the same return false
        # create a list out of all letters in word
        # sort the list alphabetically
        # check if both lists match

        list_str1 = list(s)
        list_str1.sort()
        list_str2 = list(t)
        list_str2.sort()

        return (list_str1 == list_str2)

# Runtime: 44 ms, faster than 70.69% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15 MB, less than 20.05% of Python3 online submissions for Valid Anagram.

    def isAnagram2(self, s: str, t: str) -> bool:

        # one dictionary
        # no built in functions
        # check length of words, if not matching => False
        # check character in strings
        # add character to dict as key and increment values
        # do the same for 2nd word, except subtract values for every character
        # if a key (letter) doesn't exist in dict => false
        # check values of dictionary, there should be nothing left => anagram, true

        counter = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False

        for val in counter.values():
            if val != 0:
                return False

        return True

# Runtime: 44 ms, faster than 70.69% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 45.34% of Python3 online submissions for Valid Anagram.


    def isAnagram3(self, s: str, t: str) -> bool:

            counter = {}

            if len(s) != len(t):
                return False

            for char in s:
                if char not in counter:
                    counter[char] = 1
                else:
                    counter[char] += 1

            for char in t:
                if char in counter.keys():
                    if counter[char] > 0:
                        counter[char] -= 1
                        if counter[char] == 0:
                            del counter[char]

            return False if counter else True

# Runtime: 64 ms, faster than 11.27% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 73.82% of Python3 online submissions for Valid Anagram.
