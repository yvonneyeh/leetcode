# 616. Add Bold Tag in String
"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""

class Solution:
  def addBoldTag(self, s: str, words: List[str]) -> str:
    string_length = len(s)
    result = []
    # bold[i] := True if s[i] should be bolded
    bold = [0] * n

    bold_end = -1  # s[i:bold_end] should be bolded
    for i in range(string_length):
      for word in words:
        if s[i:].startswith(word):
          bold_end = max(bold_end, i + len(word))
      bold[i] = bold_end > i

    # construct the with bold tags
    i = 0
    while i < string_length:
      if bold[i]:
        j = i
        while j < string_length and bold[j]:
          j += 1
        # s[i:j] should be bolded
        result.append('<b>' + s[i:j] + '</b>')
        i = j
      else:
        result.append(s[i])
        i += 1

    return ''.join(result)
