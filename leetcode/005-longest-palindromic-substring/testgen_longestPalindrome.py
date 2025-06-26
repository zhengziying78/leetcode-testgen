"""
Test case generator for Longest Palindromic Substring.

This module provides functionality to generate test cases for the 
Longest Palindromic Substring problem.
"""

import random
import string
from typing import List


class TestCaseGenerator:
    """Generates test cases for the Longest Palindromic Substring problem."""
    
    def __init__(self, seed: int = 42):
        """Initialize with a random seed for reproducibility."""
        random.seed(seed)
    
    def create_palindrome(self, length: int) -> str:
        """Create a palindrome of given length."""
        if length <= 0:
            return ""
        
        if length == 1:
            return random.choice(string.ascii_lowercase)
        
        # Create first half
        half_len = length // 2
        first_half = ''.join(random.choices(string.ascii_lowercase, k=half_len))
        
        # Create palindrome
        if length % 2 == 0:
            # Even length palindrome
            return first_half + first_half[::-1]
        else:
            # Odd length palindrome
            middle = random.choice(string.ascii_lowercase)
            return first_half + middle + first_half[::-1]
    
    def embed_palindrome_in_string(self, palindrome: str, total_length: int) -> str:
        """Embed a palindrome in a longer string."""
        if len(palindrome) >= total_length:
            return palindrome
        
        # Calculate prefix and suffix lengths
        remaining = total_length - len(palindrome)
        prefix_len = random.randint(0, remaining)
        suffix_len = remaining - prefix_len
        
        # Generate random prefix and suffix
        prefix = ''.join(random.choices(string.ascii_lowercase, k=prefix_len))
        suffix = ''.join(random.choices(string.ascii_lowercase, k=suffix_len))
        
        return prefix + palindrome + suffix
    
    def generate_basic_cases(self) -> List[dict]:
        """Generate basic test cases covering common scenarios."""
        cases = []
        
        # Case 1: Basic palindrome
        cases.append({
            "id": "basic_case_1",
            "description": "Basic palindrome substring",
            "input": {"s": "babad"},
            "expected": "bab"  # or "aba"
        })
        
        # Case 2: Even length palindrome
        cases.append({
            "id": "basic_case_2",
            "description": "Even length palindrome",
            "input": {"s": "cbbd"},
            "expected": "bb"
        })
        
        # Case 3: Entire string is palindrome
        cases.append({
            "id": "whole_palindrome",
            "description": "Entire string is a palindrome",
            "input": {"s": "racecar"},
            "expected": "racecar"
        })
        
        # Case 4: No palindrome longer than 1
        cases.append({
            "id": "no_long_palindrome",
            "description": "No palindrome longer than single character",
            "input": {"s": "abcd"},
            "expected": "a"  # Any single character
        })
        
        return cases
    
    def generate_edge_cases(self) -> List[dict]:
        """Generate edge case test cases."""
        cases = []
        
        # Case 1: Single character
        cases.append({
            "id": "single_char",
            "description": "Single character string",
            "input": {"s": "a"},
            "expected": "a"
        })
        
        # Case 2: Two identical characters
        cases.append({
            "id": "two_identical",
            "description": "Two identical characters",
            "input": {"s": "aa"},
            "expected": "aa"
        })
        
        # Case 3: Two different characters
        cases.append({
            "id": "two_different",
            "description": "Two different characters",
            "input": {"s": "ab"},
            "expected": "a"  # or "b"
        })
        
        # Case 4: Long string with single character
        cases.append({
            "id": "repeated_char",
            "description": "String with repeated characters",
            "input": {"s": "aaaa"},
            "expected": "aaaa"
        })
        
        return cases
    
    def find_longest_palindrome(self, s: str) -> str:
        """Helper method to find the actual longest palindrome."""
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        for i in range(len(s)):
            # Check odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1
            
            # Check even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1
        
        return s[start:start + max_len]
    
    def generate_test_cases(self, num_cases: int = 10) -> List[dict]:
        """
        Generate a comprehensive set of test cases.
        
        Args:
            num_cases: Number of additional random test cases to generate
            
        Returns:
            List of test case dictionaries
        """
        all_cases = []
        
        # Add basic cases
        all_cases.extend(self.generate_basic_cases())
        
        # Add edge cases
        all_cases.extend(self.generate_edge_cases())
        
        # Add random cases
        for i in range(num_cases):
            # Create a palindrome of random length
            palindrome_len = random.randint(2, 8)
            palindrome = self.create_palindrome(palindrome_len)
            
            # Embed it in a longer string
            total_len = random.randint(palindrome_len, 20)
            test_string = self.embed_palindrome_in_string(palindrome, total_len)
            
            # Find the actual longest palindrome (in case there are multiple)
            expected = self.find_longest_palindrome(test_string)
            
            all_cases.append({
                "id": f"random_case_{i+1}",
                "description": f"Random string with embedded palindrome",
                "input": {"s": test_string},
                "expected": expected
            })
        
        return all_cases


if __name__ == "__main__":
    generator = TestCaseGenerator()
    test_cases = generator.generate_test_cases(5)
    
    print("Generated test cases:")
    for case in test_cases:
        print(f"ID: {case['id']}")
        print(f"Description: {case['description']}")
        print(f"Input: {case['input']}")
        print(f"Expected: {case['expected']}")
        print()