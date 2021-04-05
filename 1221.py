# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Split balanced string in the maximum amount of balanced strings.
        """

        # Example 1:
        #
        # Input: s = "RLRRLLRLRL"
        # Output: 4
        # Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
        # Example 2:
        #
        # Input: s = "RLLLLRRRLR"
        # Output: 3
        # Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
        # Example 3:
        #
        # Input: s = "LLLLRRRR"
        # Output: 1
        # Explanation: s can be split into "LLLLRRRR".
        # Example 4:
        #
        # Input: s = "RLRRRLLRLL"
        # Output: 2
        # Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


        # 1. look at all characters in S - can only be L or R
        # 2. keep track of letters we have seen in a list (stack)
        # 3. count total balanced strings
        # 4. if next character is the same as current, add to stack
        # 5. if next char is different, remove from stack

        stack = []
        result = 0

        for c in s:
            if stack == []:
                result += 1
                stack.append(c)
            elif c == stack[-1]:
                stack.append(c)
            else:
                stack.pop()

        return result

# Runtime: 28 ms, faster than 82.19% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 14.3 MB, less than 12.39% of Python3 online submissions for Split a String in Balanced Strings.
