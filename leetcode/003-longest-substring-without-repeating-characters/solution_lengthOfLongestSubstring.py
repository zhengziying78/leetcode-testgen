"""
Longest Substring Without Repeating Characters solution implementation.

Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        
        Args:
            s: Input string
            
        Returns:
            int: Length of the longest substring without repeating characters
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If character is already in set, remove characters from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to set
            char_set.add(s[right])
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length