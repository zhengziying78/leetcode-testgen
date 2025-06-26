import pytest
import sys
from pathlib import Path
from solution_isMatch import Solution

# Add the leetcode directory to the path so we can import common modules
sys.path.append(str(Path(__file__).parent.parent))
from common.test_utils import load_test_cases


# Load test cases at module level
TEST_CASES = load_test_cases(__file__)


@pytest.mark.parametrize("test_case", TEST_CASES, ids=[tc["id"] for tc in TEST_CASES])
def test_isMatch(test_case):
    """Data-driven test for Regular Expression Matching problem."""
    solution = Solution()
    result = solution.isMatch(test_case["input"]["s"], test_case["input"]["p"])
    
    # Verify result matches expected
    expected = test_case["expected"]
    assert result == expected