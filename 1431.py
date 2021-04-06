# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result

# Runtime: 40 ms, faster than 49.66% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 14.3 MB, less than 22.83% of Python3 online submissions for Kids With the Greatest Number of Candies.
