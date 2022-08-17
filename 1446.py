class Solution:
    def maxPower(self, s: str) -> int:
        previous = ''
        count = 1
        max_count = 0
        for letter in s:
            if letter == previous:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
            previous = letter

        return max(max_count, count)

    class Solution:
    def maxPower(self, s: str) -> int:
        max_count, count = 0, 1
        char = ""
        for i in s:
            if char == i:
                count += 1
            else:
                count = 1
            char = i
            max_count = max(max_count, count)
        return max_count
