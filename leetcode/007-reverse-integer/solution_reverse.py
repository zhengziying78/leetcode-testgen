"""
Reverse Integer solution implementation.

Source: https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse digits of a 32-bit signed integer.
        
        Args:
            x: Input integer
            
        Returns:
            int: Reversed integer, or 0 if overflow occurs
        """
        # Handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        result = 0
        while x:
            digit = x % 10
            x //= 10
            
            # Check for overflow before updating result
            # 32-bit signed integer range: -2^31 to 2^31 - 1
            if result > (2**31 - 1) // 10:
                return 0
            if result == (2**31 - 1) // 10 and digit > (2**31 - 1) % 10:
                return 0
            
            result = result * 10 + digit
        
        result *= sign
        
        # Final overflow check
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result