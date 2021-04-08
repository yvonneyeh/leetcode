1704. Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:

# make all letters lower cased
# divide word in half - calc length of word
# split string into first half and 2nd half
# count number of vowels in 1 and 2
# compare total, if same number return true, if not false

        vowels = "aeiou"

        half = len(s)//2
        # print(half)

        s1 = s[:half].lower()
        s2 = s[half:].lower()

        count1 = 0
        count2 = 0
        # print(s1, s2)

        for letter in s1:
            if letter in vowels:
                count1 += 1

        for letter in s2:
            if letter in vowels:
                count2 += 1

        return count1 == count2

# Runtime: 36 ms, faster than 56.88% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 14.4 MB, less than 37.61% of Python3 online submissions for Determine if String Halves Are Alike.

    def halvesAreAlike2(self, s: str) -> bool:

        vowels = set("aeiouAEIOU")

        count1 = 0
        count2 = 0
        i = 0
        j = len(s) - 1

        while i < j:
            count1 += s[i] in vowels
            count2 += s[j] in vowels
            i += 1
            j -= 1

        return count1 == count2

# Runtime: 36 ms, faster than 56.88% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 14.1 MB, less than 88.26% of Python3 online submissions for Determine if String Halves Are Alike.
