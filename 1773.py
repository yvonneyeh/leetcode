class Solution:
    def countMatches2ndTry(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

# 1. look at key and value, keep track of it
# 2. index into the lists to check if both the key and value match
# 3. count number of items matching (counter of some sort)
# 4. return the number of items matching

# #  list[a][b]

# list[[type, color, item]]
# type = list[x][0]
# color = list[x][1]
# item = list[x][2]
        dict = {
            'type':0,
            'color':1,
            'name':2
        }
        matches = 0
        for item in items:
            if ruleValue == item[dict[ruleKey]]:
                matching += 1

        return matching

# Runtime: 232 ms, faster than 93.91% of Python3 online submissions for Count Items Matching a Rule.
# Memory Usage: 20.7 MB, less than 21.33% of Python3 online submissions for Count Items Matching a Rule.


    def countMatches_1stTry(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        matching = 0
        for item in items:
            if ruleKey == 'type':
                if ruleValue == item[0]:
                    matching += 1
            if ruleKey == 'color':
                if ruleValue == item[1]:
                    matching += 1
            if ruleKey == 'name':
                if ruleValue == item[2]:
                    matching += 1

        return matching


# Runtime: 240 ms, faster than 73.55% of Python3 online submissions for Count Items Matching a Rule.
# Memory Usage: 20.6 MB, less than 21.33% of Python3 online submissions for Count Items Matching a Rule.
