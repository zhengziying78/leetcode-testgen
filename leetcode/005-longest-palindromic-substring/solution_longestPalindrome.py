"""
Longest Palindromic Substring solution implementation.

Source: https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in a given string.
        
        Args:
            s: Input string
            
        Returns:
            str: The longest palindromic substring
            
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        for i in range(len(s)):
            # Check for odd-length palindromes (center is s[i])
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1
            
            # Check for even-length palindromes (center is between s[i] and s[i+1])
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1
        
        return s[start:start + max_len]
    
    def longestPalindrome_dp(self, s: str) -> str:
        """
        Alternative solution using dynamic programming.
        
        Args:
            s: Input string
            
        Returns:
            str: The longest palindromic substring
            
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        if not s:
            return ""
        
        n = len(s)
        # dp[i][j] represents whether s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_len = 1
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        # Check for palindromes of length 3 and more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Check if s[i:j+1] is palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start:start + max_len]