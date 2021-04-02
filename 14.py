# 14. Longest Common Prefix

# class Solution:
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str

    # 1. output = ""
    # 2. look at all the words in the list
    # 3. check index[0] for all words
    # 4. case 1: if there isn't any, return empty string
    # 5. case 2: if first letter matches for all words,
    #     add that letter to the output
    # 6. case 3: keep adding letters to the output

    # output = ""
    # n = 0
    # num_words = len(strs)
    #
    # for word in strs:
    #     if
    # if not strs: return ""
    """
    prefix = ''
    # * is the unpacking operator, essential here
    for z in zip(*strs):
        # print(z)
        letters = set(z)
        if len(letters) == 1:
            # print(len(letters))
            prefix += letters.pop()
        else:
            break
    return prefix


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

# Runtime: 36 ms, faster than 52.54% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.4 MB, less than 58.16% of Python3 online submissions for Longest Common Prefix.
