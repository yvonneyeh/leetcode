# 224. Basic Calculator
# Given a string s representing an expression, implement a basic calculator to evaluate it.

# https://www.youtube.com/watch?v=081AqOuasw0

def calculate(self, s: str) -> int:
        """
        1. Take 3 containers:
        num -> to store current num value only
        sign -> to store sign value, initially +1
        res -> to store sum
        When ( comes these containers used for calculate sum of intergers within () brackets.
        --------------------
        2. When c is + or -
        Move num to res, because we need to empty num for next integer value.
        set num = 0
        sign = update with c
        --------------------
        3. When c is '('
        Here, we need num, res, sign to calculate sum of integers within ()
        So, move num and sign to stack => [num, sign]
        Now reset - res = 0, num = 0, sign = 1 (default)
        --------------------
        4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
        res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
        res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
        res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
        --------------------
        Simple Example: 2 - 3
        Initially res will have 2,i.e. res = 2
        then store '-' in sign. it will be used when 3 comes. ie. sign = -1
        Now 3 comes => res = res + num*sign
        Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
        """
        num = 0
        sign = 1
        res = 0
        stack = []
        for i in range(len(s)): # iterate till last character
            c = s[i]
            if c.isdigit(): # process if there is digit
                num = num*10 + int(c) # for consecutive digits 98 => 9x10 + 8 = 98
            elif c in '-+': # check for - and +
                res += num*sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res +=sign*num
                res *=stack.pop()
                res +=stack.pop()
                num = 0
        return res + num*sign

# Runtime: 76 ms, faster than 69.35% of Python3 online submissions for Basic Calculator.
# Memory Usage: 15.7 MB, less than 63.10% of Python3 online submissions for Basic Calculator.

class Solution:
    def calculate(self, s: str) -> int:

        # only digits, +, -, (), ' '
        # we will ignore spaces
        # keep track of current sum
        # can only be plus or minus, keep track of positive or neg sign
        # use stack to keep track of calls waiting to happen
        # append items to stack to keep track of what hasn't happened
        # pop items from stack once we see close paren


        stack = []
        result = 0
        num = 0
        sign = 1

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '+-':
                result += num*sign
                sign = -1 if c == '-' else 1
                num = 0
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result +=sign*num
                result *=stack.pop()
                result +=stack.pop()
                num = 0
        return result + num*sign


    def withQuincy(s):

        stack = []
        result = 0
        num = ""
        sign = 1

        for char in s:
            if char == '-':
        	    sign = -1
            if char.isdigit():
                num += char
            elif num != "":
                if char in '+-':
                    result += num*sign
                    sign = -1 if char == '-' else 1
                    num = ""
                elif char == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif char == ')':
                    result +=sign*num
                    result *=stack.pop()
                    result +=stack.pop()
                    num = ""

        return result + num*sign
