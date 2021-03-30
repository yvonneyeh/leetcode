class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000,
                'IV':4,
                'IX':9,
                'XL':40,
                'XC':90,
                'CD':400,
                'CM':900,
                }

        i = 0
        sum = 0

        while i < len(s):
            s1 = s[i] # current char
            s2 = s[i:i+2] # current and next char

            # if current char and next char combo present in dictionary
            if s2 in roman:
                sum += roman[s2]
                i += 2
            else:
                sum += roman[s1]
                i += 1

        return sum

# take in a string of roman numerals
# convert roman to integer
# I > 1
# V > 5
# X > 10
# L > 50
# C > 100
# D > 500
# M > 1000

# test cases
# none: always input roman numerals
# one -
# input: I
# output 1
# many -
# input: IV
# output: 4
# input: LVIII
# output = 58
# L = 50, V = 5, III = 3

# break down number into pieces
# variable "sum" start at 0
# check if M is in s:
    # if "CM" - add 900
    # if not then add 1000
# same for D, C, L, X, V,
# if I exists in S:
# if IV exists > 4
# I = 1
# len
