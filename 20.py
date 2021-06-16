# 20. Valid Parentheses
# Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:

        # add items from string into list
        # create stack
        # check if paren is in open list
        # if not, check if last item in stack matches closed paren
        # pop items off stack if match
        # if stack length is zero then it is valid

        opened = ['(','{','[']
        closed = [')','}',']']
        stack = []

        for paren in s:
            if paren in opened:
                stack.append(paren)
            else:
                if len(stack) != 0 and stack[-1] == opened[closed.index(paren)]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
