# 214. Shortest Palindrome

def shortestPalindrome(s):

        # reverse string
        r = s[::-1]
        print(r)

        # loop through
        for i in range(len(s) + 1):
            print(i)
            if s.startswith(r[i:]):
                print(r[i:])
                print(r[:i] + s)
                return r[:i] + s

s = "abcd"
shortestPalindrome(s)
