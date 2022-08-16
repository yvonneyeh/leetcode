class Solution:
    def defangIPaddrString(self, address: str) -> str:


        # 1. look at every char of string
        # 2. keep track of the new address
        # 3. if the char is . then replace with [.]
        # 4. if char is not . then add the char to new address
        # 5. return new address

        defangIP = ""

        for char in address:
            if char != ".":
                defangIP += char
            if char == ".":
                defangIP += "[.]"
        return defangIP

    def defangIPaddrList(self, address: str) -> str:
        result = []
        for character in address:
            if character == '.':
                result.append('[.]')
            else:
                result.append(character)
        return ''.join(result)


# Runtime: 28 ms, faster than 78.88% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.3 MB, less than 35.09% of Python3 online submissions for Defanging an IP Address.
#

    def defangIPaddr_replace(self, address: str) -> str:

        return address.replace('.','[.]')
#
# Runtime: 24 ms, faster than 93.90% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14 MB, less than 87.04% of Python3 online submissions for Defanging an IP Address.
