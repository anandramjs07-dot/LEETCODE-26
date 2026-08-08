class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits
        num = 0

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        # 4. Check 32-bit range
        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num