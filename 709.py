# 709. To Lower Case

class Solution:
    def toLowerCase(self, str: str) -> str:

        # iterate through string
        # new_str = ""
        # convert letter to lower case
        # add lower letter to new string
        # return new string

        new_str = ""

        for s in str:
            new_str += s.lower()

        return new_str
