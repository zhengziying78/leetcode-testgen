"""
Test cases for testgen_twoSum module.
"""

import pytest
from testgen_twoSum import (
    TargetStrategy,
    GoldenNumberStrategy,
    LengthStrategy,
    pick_target,
    pick_golden_numbers,
    pick_length,
    LENGTH_MIN,
    LENGTH_MAX
)


def test_pick_golden_numbers():
    """Test pick_golden_numbers with all strategy combinations."""
    for target_strategy in TargetStrategy:
        for golden_strategy in GoldenNumberStrategy:
            target = pick_target(target_strategy)
            num1, num2 = pick_golden_numbers(target, golden_strategy)
            assert num1 + num2 == target, f"Failed for target_strategy={target_strategy}, golden_strategy={golden_strategy}, target={target}, nums=({num1}, {num2})"


def test_pick_length():
    """Test pick_length with all strategies."""
    for length_strategy in LengthStrategy:
        length = pick_length(length_strategy)
        assert LENGTH_MIN <= length <= LENGTH_MAX, f"Failed for length_strategy={length_strategy}, length={length}"