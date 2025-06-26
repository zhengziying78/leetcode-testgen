"""
Regular Expression Matching solution implementation.

Source: https://leetcode.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Implement regular expression matching with support for '.' and '*'.
        
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        
        Args:
            s: Input string
            p: Pattern string
            
        Returns:
            bool: True if s matches the pattern p, False otherwise
        """
        m, n = len(s), len(p)
        
        # dp[i][j] represents if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* etc.
        # These can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * can match zero or more of the preceding element
                    # Case 1: * matches zero occurrences (ignore x*)
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: * matches one or more occurrences
                    # Check if preceding character matches current character in s
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    # Regular character or '.'
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]