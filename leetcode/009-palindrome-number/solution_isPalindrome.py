"""
Palindrome Number solution implementation.

Source: https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Determine whether an integer is a palindrome without converting to string.
        
        Args:
            x: Input integer
            
        Returns:
            bool: True if x is a palindrome, False otherwise
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Single digit numbers are palindromes
        if x < 10:
            return True
        
        # Numbers ending in 0 (except 0) are not palindromes
        if x % 10 == 0:
            return False
        
        # Reverse the number mathematically and compare
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return original == reversed_num