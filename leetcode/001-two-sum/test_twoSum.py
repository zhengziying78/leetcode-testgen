import pytest
from twoSum import Solution


def test_twoSum_dummy():
    """
    Dummy test case for twoSum method.
    Just invokes the method with dummy input without checking output.
    """
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    
    # Call the method but don't assert anything
    result = solution.twoSum(nums, target)