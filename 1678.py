# 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        o = command.replace("()", "o")
        al = o.replace("(al)","al")

        return al

# Runtime: 24 ms, faster than 94.29% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.3 MB, less than 40.58% of Python3 online submissions for Goal Parser Interpretation.

    def interpret2(self, command: str) -> str:

        return command.replace("()", "o").replace("(al)","al")

# Runtime: 24 ms, faster than 94.29% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.1 MB, less than 69.98% of Python3 online submissions for Goal Parser Interpretation.
