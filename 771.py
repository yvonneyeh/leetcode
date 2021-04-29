# 771. Jewels and Stones
# Easy
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = 0
        for jewel in stones:
            if jewel in jewels:
                count += 1

        return count

# Runtime: 32 ms, faster than 54.43% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.3 MB, less than 45.91% of Python3 online submissions for Jewels and Stones.


    def numJewelsInStones2(self, jewels: str, stones: str) -> int:

        return sum(i in jewels for i in stones)

# Runtime: 28 ms, faster than 81.10% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14.3 MB, less than 45.91% of Python3 online submissions for Jewels and Stones.
