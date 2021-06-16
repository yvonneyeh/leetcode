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

        # Runtime: 28 ms


    def isValid_dict(self, s: str) -> bool:

        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for paren in s:
            if paren in match:
                if not (stack and stack.pop() == match[paren]):
                    return False
            else:
                stack.append(paren)
        return not stack

    # Runtime: 28 ms
