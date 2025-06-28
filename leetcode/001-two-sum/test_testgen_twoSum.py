"""
Test cases for testgen_twoSum module.
"""

import pytest
import itertools
from testgen_twoSum import (
    TargetStrategy,
    GoldenNumberStrategy,
    LengthStrategy,
    ReorderStrategy,
    pick_target,
    pick_golden_numbers,
    pick_length,
    ALL_STRATEGY_COMBINATIONS,
    LENGTH_MIN,
    LENGTH_MAX,
    NUM_MIN,
    NUM_MAX
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


def test_all_strategy_combinations_completeness():
    """Test that ALL_STRATEGY_COMBINATIONS matches the full itertools product."""
    # Generate expected combinations using itertools
    expected_combinations = list(itertools.product(
        list(TargetStrategy),
        list(GoldenNumberStrategy),
        list(LengthStrategy),
        list(ReorderStrategy)
    ))
    
    # Convert to sets for comparison (order doesn't matter)
    expected_set = set(expected_combinations)
    actual_set = set(ALL_STRATEGY_COMBINATIONS)
    
    # Check counts
    assert len(ALL_STRATEGY_COMBINATIONS) == 486, f"Expected 486 combinations, got {len(ALL_STRATEGY_COMBINATIONS)}"
    assert len(expected_combinations) == 486, f"Expected 486 combinations from itertools, got {len(expected_combinations)}"
    
    # Check that all expected combinations are present
    missing_combinations = expected_set - actual_set
    assert not missing_combinations, f"Missing combinations: {missing_combinations}"
    
    # Check that no extra combinations are present
    extra_combinations = actual_set - expected_set
    assert not extra_combinations, f"Extra combinations: {extra_combinations}"
    
    # Final verification: sets should be identical
    assert actual_set == expected_set, "ALL_STRATEGY_COMBINATIONS does not match itertools product"