# 3. Longest Substring Without Repeating Characters

"""
Medium

Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    def lengthOfLongestSubstring_dict(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0
        for end, character in enumerate(s):
            if character in seen and start <= seen[character]:
                start = seen[character] + 1
            else:
                max_length = max(max_length, end - start + 1)

            seen[character] = end

        return max_length

    def lengthOfLongestSubstring_set(self, s: str) -> int:
        # keep track of start and end index for substring
        # use dictionary to save letters we've seen
        # save longest length

        start = 0
        seen = set()
        longest = 0

        for end, letter in enumerate(s):
            while letter in seen:
                seen.remove(s[start])
                start += 1
            seen.add(letter)
            longest = max(longest, end - start + 1)

        return longest
