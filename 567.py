# 567. Permutation in String
"""
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

# 1. Create a HashMap to calculate the frequencies of all characters in the pattern.
# 2. Iterate through the string, adding one character at a time in the sliding window.
# 3. If the character being added matches a character in the HashMap, decrement its frequency in the map. If the character frequency becomes zero, we got a complete match.
# 4. If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e., total characters in the HashMap), we have gotten our required permutation.
# 5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s size. At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.

class Solution:
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        pattern = s1
        text = s2
        frequency = {}
        window_start = 0
        matches = 0

        for letter in pattern:
            frequency[letter] = frequency.get(letter, 0) + 1

        for window_end, right_letter in enumerate(text):
            if right_letter in frequency:
                frequency[right_letter] -= 1
                if frequency[right_letter] == 0:
                    matches += 1

            if matches == len(frequency):
                return True

            if window_end >= len(pattern) - 1:
                left_letter = text[window_start]
                window_start += 1
                if left_letter in frequency:
                    if frequency[left_letter] == 0:
                        matches -= 1
                    frequency[left_letter] += 1

        return False

    # Runtime: 76 ms
    # Memory: 14 MB


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1_count = Counter(s1)

        for i in range(len(s2) - window + 1):
            s2_count = Counter(s2[i:i+window])
            if s2_count == s1_count:
                return True

        return False

    # Runtime: 2450 ms
    # Memory: 13.7 MB
