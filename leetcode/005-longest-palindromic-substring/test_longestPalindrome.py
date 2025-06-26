import pytest
import sys
from pathlib import Path
from solution_longestPalindrome import Solution

# Add the leetcode directory to the path so we can import common modules
sys.path.append(str(Path(__file__).parent.parent))
from common.test_utils import load_test_cases


# Load test cases at module level
TEST_CASES = load_test_cases(__file__)


def is_palindrome(s: str) -> bool:
    """Helper function to check if a string is a palindrome."""
    return s == s[::-1]


@pytest.mark.parametrize("test_case", TEST_CASES, ids=[tc["id"] for tc in TEST_CASES])
def test_longest_palindrome(test_case):
    """Data-driven test for Longest Palindromic Substring problem."""
    solution = Solution()
    result = solution.longestPalindrome(test_case["input"]["s"])
    expected = test_case["expected"]
    
    # Verify result is a palindrome
    assert is_palindrome(result), f"Result '{result}' is not a palindrome"
    
    # Verify result length is at least as long as expected
    assert len(result) >= len(expected), f"Result length {len(result)} is less than expected {len(expected)}"
    
    # For deterministic test cases, check exact match
    if test_case["id"] in ["single_char", "two_identical", "repeated_char", "whole_palindrome"]:
        assert result == expected, f"Expected '{expected}', got '{result}'"
    
    # For cases where multiple answers are possible, just verify it's a valid palindrome
    # and is present in the original string
    input_string = test_case["input"]["s"]
    assert result in input_string, f"Result '{result}' not found in input string '{input_string}'"