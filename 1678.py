# 1678. Goal Parser Interpretation

class Solution:
    def interpret(self, command: str) -> str:
        o = command.replace("()", "o")
        al = o.replace("(al)","al")

        return al

# Runtime: 24 ms, faster than 94.29% of Python3 online submissions for Goal Parser Interpretation.
# Memory Usage: 14.3 MB, less than 40.58% of Python3 online submissions for Goal Parser Interpretation.
