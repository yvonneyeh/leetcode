# 1614. Maximum Nesting Depth of the Parentheses

# look at every character in string
# if char = ( add to stack
# if char = ) remove ( from stack
# keep counter for stack and for max depth

class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        count = 0
        max = 0

        for c in s:
            if c == "(":
                stack.append(c)
                count += 1
                if count > max:
                    max = count
            if c == ")":
                stack.pop()
                count -= 1
        return max


# Runtime: 32 ms, faster than 52.44% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
# Memory Usage: 14.3 MB, less than 41.39% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
