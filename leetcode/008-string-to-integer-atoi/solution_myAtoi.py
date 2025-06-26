"""
String to Integer (atoi) solution implementation.

Source: https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
        
        Args:
            s: Input string
            
        Returns:
            int: Converted integer, clamped to 32-bit signed integer range
        """
        if not s:
            return 0
        
        # Step 1: Skip leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        if i == len(s):
            return 0
        
        # Step 2: Handle sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Parse digits and handle overflow
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before updating result
            # 32-bit signed integer range: -2^31 to 2^31 - 1
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31
            
            # Check if result would overflow on next multiplication
            if result > INT_MAX // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            # Check if result would overflow on next addition
            if result == INT_MAX // 10:
                if sign == 1 and digit > INT_MAX % 10:
                    return INT_MAX
                if sign == -1 and digit > -(INT_MIN % 10):
                    return INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        result *= sign
        
        # Final clamp to 32-bit range
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
            
        return result