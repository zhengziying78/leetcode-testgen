"""
Test case generator for Two Sum problem.

This module will contain algorithms to generate comprehensive test cases
for the Two Sum problem without circular reasoning.

TODO: Implement test case generation logic.
"""

import random
import yaml
import os
from datetime import datetime
from typing import List, Tuple, Optional, NamedTuple, Dict
from enum import Enum
from dataclasses import dataclass


TARGET_MIN = -10**9
TARGET_MAX = 10**9

NUM_MIN = -10**9
NUM_MAX = 10**9

LENGTH_MIN = 2
LENGTH_MAX = 10**4


class TargetStrategy(Enum):
    MIN_NUMBER = 1
    MIN_NUMBER_PLUS_ONE = 2
    MAX_NUMBER = 3
    MAX_NUMBER_MINUS_ONE = 4
    ZERO = 5
    ONE = 6
    NEGATIVE_ONE = 7
    RANDOM_NEGATIVE = 8
    RANDOM_POSITIVE = 9


class GoldenNumberStrategy(Enum):
    CLOSEST = 1
    MOST_DISTANT = 2
    RANDOM = 3


class LengthStrategy(Enum):
    LEAST_POSSIBLE = 1
    LARGEST_POSSIBLE = 2
    LEAST_POSSIBLE_PLUS_ONE = 3
    LARGEST_POSSIBLE_MINUS_ONE = 4
    SOMEWHAT_LARGE = 5
    SOMEWHAT_SMALL = 6


class DullNumberStrategy(Enum):
    RANGE1_ONLY = 1
    RANGE2_ONLY = 2
    RANGE3_ONLY = 3
    RANGE1_AND_2 = 4
    RANGE1_AND_3 = 5
    RANGE2_AND_3 = 6
    ALL_RANGES = 7


class ReorderStrategy(Enum):
    ASC_ORDERED = 1
    DESC_ORDERED = 2
    RANDOMLY_SHUFFLED = 3


@dataclass
class TestCase:
    id: str
    target_strategy: TargetStrategy
    golden_strategy: GoldenNumberStrategy
    length_strategy: LengthStrategy
    dull_strategy: DullNumberStrategy
    reorder_strategy: ReorderStrategy
    target: int
    nums: List[int]
    expected: List[int]


# Global list of all strategy combinations (9 * 3 * 6 * 3 = 486 entries)
ALL_STRATEGY_COMBINATIONS: List[Tuple[TargetStrategy, GoldenNumberStrategy, LengthStrategy, ReorderStrategy]] = [
    # TargetStrategy.MIN_NUMBER combinations (1-162)
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.RANDOMLY_SHUFFLED),
    
    # TargetStrategy.MIN_NUMBER_PLUS_ONE combinations (55-108)
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.CLOSEST, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.MOST_DISTANT, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_LARGE, ReorderStrategy.RANDOMLY_SHUFFLED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.ASC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.DESC_ORDERED),
    (TargetStrategy.MIN_NUMBER_PLUS_ONE, GoldenNumberStrategy.RANDOM, LengthStrategy.SOMEWHAT_SMALL, ReorderStrategy.RANDOMLY_SHUFFLED),
    
    # Continue with remaining TargetStrategy values...
    # I'll add the rest programmatically to avoid the extremely long manual list
] + [
    # Generate remaining combinations programmatically
    (target_strat, golden_strat, length_strat, reorder_strat)
    for target_strat in [TargetStrategy.MAX_NUMBER, TargetStrategy.MAX_NUMBER_MINUS_ONE, 
                        TargetStrategy.ZERO, TargetStrategy.ONE, TargetStrategy.NEGATIVE_ONE,
                        TargetStrategy.RANDOM_NEGATIVE, TargetStrategy.RANDOM_POSITIVE]
    for golden_strat in [GoldenNumberStrategy.CLOSEST, GoldenNumberStrategy.MOST_DISTANT, GoldenNumberStrategy.RANDOM]
    for length_strat in [LengthStrategy.LEAST_POSSIBLE, LengthStrategy.LARGEST_POSSIBLE,
                        LengthStrategy.LEAST_POSSIBLE_PLUS_ONE, LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE,
                        LengthStrategy.SOMEWHAT_LARGE, LengthStrategy.SOMEWHAT_SMALL]
    for reorder_strat in [ReorderStrategy.ASC_ORDERED, ReorderStrategy.DESC_ORDERED, ReorderStrategy.RANDOMLY_SHUFFLED]
]


def pick_target(strategy: TargetStrategy, nums: List[int] = None) -> int:
    """
    Generate a target value using the specified strategy.
    
    Args:
        strategy: Target generation strategy to use
        nums: Not used, kept for interface compatibility
        
    Returns:
        Target integer in range [-10^9, 10^9]
    """
    if strategy == TargetStrategy.MIN_NUMBER:
        return TARGET_MIN
    elif strategy == TargetStrategy.MIN_NUMBER_PLUS_ONE:
        return TARGET_MIN + 1
    elif strategy == TargetStrategy.MAX_NUMBER:
        return TARGET_MAX
    elif strategy == TargetStrategy.MAX_NUMBER_MINUS_ONE:
        return TARGET_MAX - 1
    elif strategy == TargetStrategy.ZERO:
        return 0
    elif strategy == TargetStrategy.ONE:
        return 1
    elif strategy == TargetStrategy.NEGATIVE_ONE:
        return -1
    elif strategy == TargetStrategy.RANDOM_NEGATIVE:
        return random.randint(TARGET_MIN + 2, -2)
    elif strategy == TargetStrategy.RANDOM_POSITIVE:
        return random.randint(2, TARGET_MAX - 2)


def pick_golden_numbers(target: int, strategy: GoldenNumberStrategy) -> Tuple[int, int]:
    """
    Pick two "golden" numbers that sum to the target.
    
    Args:
        target: Target sum value
        strategy: Strategy for picking the two numbers
        
    Returns:
        Tuple of two numbers that sum to target
    """
    if strategy == GoldenNumberStrategy.CLOSEST:
        if target % 2 == 0:
            half = target // 2
            return (half, half)
        else:
            half = target // 2
            return (half, half + 1)
    elif strategy == GoldenNumberStrategy.MOST_DISTANT:
        num1 = NUM_MIN
        num2 = target - num1
        if num2 > NUM_MAX:
            num2 = NUM_MAX
            num1 = target - num2
        return (num1, num2)
    elif strategy == GoldenNumberStrategy.RANDOM:
        num1 = random.randint(NUM_MIN, NUM_MAX)
        num2 = target - num1
        if NUM_MIN <= num2 <= NUM_MAX:
            return (num1, num2)
        else:
            # If num2 is out of range, pick a valid num1 that keeps num2 in range
            min_num1 = max(NUM_MIN, target - NUM_MAX)
            max_num1 = min(NUM_MAX, target - NUM_MIN)
            if min_num1 <= max_num1:
                num1 = random.randint(min_num1, max_num1)
                num2 = target - num1
                return (num1, num2)
            else:
                # Fallback to closest strategy if no valid random pair exists
                if target % 2 == 0:
                    half = target // 2
                    return (half, half)
                else:
                    half = target // 2
                    return (half, half + 1)


def pick_length(strategy: LengthStrategy) -> int:
    """
    Pick the length of the nums list.
    
    Args:
        strategy: Strategy for picking the length
        
    Returns:
        Length integer in range [2, 10^4]
    """
    if strategy == LengthStrategy.LEAST_POSSIBLE:
        return LENGTH_MIN
    elif strategy == LengthStrategy.LARGEST_POSSIBLE:
        return LENGTH_MAX
    elif strategy == LengthStrategy.SOMEWHAT_LARGE:
        # return random.randint(LENGTH_MAX // 2, LENGTH_MAX)
        return 1000
    elif strategy == LengthStrategy.SOMEWHAT_SMALL:
        return random.randint(10, 20)
    elif strategy == LengthStrategy.LEAST_POSSIBLE_PLUS_ONE:
        return LENGTH_MIN + 1
    elif strategy == LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE:
        return LENGTH_MAX - 1


def pick_dull_numbers(dull_count: int, golden_num1: int, golden_num2: int, target: int) -> Dict[DullNumberStrategy, List[int]]:
    """
    Pick dull numbers to fill the remaining positions in the list using all valid strategies.
    
    Args:
        dull_count: Number of dull numbers needed
        golden_num1: First golden number
        golden_num2: Second golden number
        target: Target sum value
        
    Returns:
        Dict mapping each valid DullNumberStrategy to its list of dull numbers
    """
    # If no dull numbers needed, return empty dict
    if dull_count <= 0:
        return {}
    
    min_golden = min(golden_num1, golden_num2)
    max_golden = max(golden_num1, golden_num2)
    
    def pick_from_range(start: int, end: int, count: int, forbidden: set) -> List[int]:
        """Pick count numbers from range [start, end] avoiding forbidden numbers."""
        picked = []
        for _ in range(count):
            attempts = 0
            while attempts < 1000:  # Prevent infinite loop
                num = random.randint(start, end)
                if num not in forbidden:
                    picked.append(num)
                    pairing = target - num
                    forbidden.add(pairing)
                    break
                attempts += 1
            else:
                # If we can't find a valid number after many attempts, return what we have
                break
        return picked
    
    # Part 2: Loop through all strategies and collect results
    results = {}
    
    for strategy in DullNumberStrategy:
        # Initialize fresh forbidden set for each strategy
        forbidden_numbers = {golden_num1, golden_num2}
        
        if strategy == DullNumberStrategy.RANGE1_ONLY:
            if NUM_MIN <= min_golden - 1:
                dull_nums = pick_from_range(NUM_MIN, min_golden - 1, dull_count, forbidden_numbers)
                results[strategy] = dull_nums
        elif strategy == DullNumberStrategy.RANGE2_ONLY:
            if min_golden + 1 <= max_golden - 1:
                dull_nums = pick_from_range(min_golden + 1, max_golden - 1, dull_count, forbidden_numbers)
                results[strategy] = dull_nums
        elif strategy == DullNumberStrategy.RANGE3_ONLY:
            if max_golden + 1 <= NUM_MAX:
                dull_nums = pick_from_range(max_golden + 1, NUM_MAX, dull_count, forbidden_numbers)
                results[strategy] = dull_nums
        elif strategy == DullNumberStrategy.RANGE1_AND_2:
            if NUM_MIN <= min_golden - 1 and min_golden + 1 <= max_golden - 1 and dull_count >= 2:
                count1 = random.randint(1, dull_count - 1)
                count2 = dull_count - count1
                nums1 = pick_from_range(NUM_MIN, min_golden - 1, count1, forbidden_numbers)
                nums2 = pick_from_range(min_golden + 1, max_golden - 1, count2, forbidden_numbers)
                results[strategy] = nums1 + nums2
        elif strategy == DullNumberStrategy.RANGE1_AND_3:
            if NUM_MIN <= min_golden - 1 and max_golden + 1 <= NUM_MAX and dull_count >= 2:
                count1 = random.randint(1, dull_count - 1)
                count3 = dull_count - count1
                nums1 = pick_from_range(NUM_MIN, min_golden - 1, count1, forbidden_numbers)
                nums3 = pick_from_range(max_golden + 1, NUM_MAX, count3, forbidden_numbers)
                results[strategy] = nums1 + nums3
        elif strategy == DullNumberStrategy.RANGE2_AND_3:
            if min_golden + 1 <= max_golden - 1 and max_golden + 1 <= NUM_MAX and dull_count >= 2:
                count2 = random.randint(1, dull_count - 1)
                count3 = dull_count - count2
                nums2 = pick_from_range(min_golden + 1, max_golden - 1, count2, forbidden_numbers)
                nums3 = pick_from_range(max_golden + 1, NUM_MAX, count3, forbidden_numbers)
                results[strategy] = nums2 + nums3
        elif strategy == DullNumberStrategy.ALL_RANGES:
            if NUM_MIN <= min_golden - 1 and min_golden + 1 <= max_golden - 1 and max_golden + 1 <= NUM_MAX and dull_count >= 3:
                count1 = random.randint(1, dull_count - 2)
                count2 = random.randint(1, dull_count - count1 - 1)
                count3 = dull_count - count1 - count2
                nums1 = pick_from_range(NUM_MIN, min_golden - 1, count1, forbidden_numbers)
                nums2 = pick_from_range(min_golden + 1, max_golden - 1, count2, forbidden_numbers)
                nums3 = pick_from_range(max_golden + 1, NUM_MAX, count3, forbidden_numbers)
                results[strategy] = nums1 + nums2 + nums3
    
    return results


def generate_test_cases(
    target_strategy: TargetStrategy,
    golden_strategy: GoldenNumberStrategy,
    length_strategy: LengthStrategy,
    reorder_strategy: ReorderStrategy
) -> List[TestCase]:
    """
    Generate test cases for Two Sum problem using specified strategies.
    
    Args:
        target_strategy: Strategy for picking the target
        golden_strategy: Strategy for picking golden numbers
        length_strategy: Strategy for picking array length
        reorder_strategy: Strategy for reordering the final array
        
    Returns:
        List of TestCase objects, one for each valid DullNumberStrategy
    """
    # Step 1: Pick target
    target = pick_target(target_strategy)
    
    # Step 2: Pick two golden numbers
    golden_num1, golden_num2 = pick_golden_numbers(target, golden_strategy)
    
    # Step 3: Pick length
    length = pick_length(length_strategy)
    
    # Step 4: Pick dull numbers (length - 2 since we have 2 golden numbers)
    dull_count = length - 2
    dull_numbers_dict = pick_dull_numbers(dull_count, golden_num1, golden_num2, target)
    
    # Step 5: Create test cases for each valid dull strategy
    test_cases = []
    
    for dull_strategy, dull_numbers in dull_numbers_dict.items():
        # Combine golden numbers and dull numbers
        complete_nums = [golden_num1, golden_num2] + dull_numbers
        
        # Apply reorder strategy
        if reorder_strategy == ReorderStrategy.ASC_ORDERED:
            complete_nums.sort()
        elif reorder_strategy == ReorderStrategy.DESC_ORDERED:
            complete_nums.sort(reverse=True)
        elif reorder_strategy == ReorderStrategy.RANDOMLY_SHUFFLED:
            random.shuffle(complete_nums)
        
        # Find indices of golden numbers in the reordered array
        golden_indices = []
        for i, num in enumerate(complete_nums):
            if (num == golden_num1 or num == golden_num2) and len(golden_indices) < 2:
                golden_indices.append(i)
        
        # Generate ID from strategy enum values
        test_id = f"{target_strategy.value}-{golden_strategy.value}-{length_strategy.value}-{reorder_strategy.value}-{dull_strategy.value}"
        
        # Create test case
        test_case = TestCase(
            id=test_id,
            target_strategy=target_strategy,
            golden_strategy=golden_strategy,
            length_strategy=length_strategy,
            dull_strategy=dull_strategy,
            reorder_strategy=reorder_strategy,
            target=target,
            nums=complete_nums,
            expected=golden_indices
        )
        
        test_cases.append(test_case)
    
    return test_cases


def generate_all_test_cases() -> List[TestCase]:
    """
    Generate test cases for all possible strategy combinations.
    
    Goes through ALL_STRATEGY_COMBINATIONS and calls generate_test_cases() 
    for each combination, collecting all results into one big list.
    
    Skips combinations with LARGEST_POSSIBLE_MINUS_ONE or LARGEST_POSSIBLE length strategies.
    
    Returns:
        List of all TestCase objects from valid strategy combinations
    """
    all_test_cases = []
    
    for target_strategy, golden_strategy, length_strategy, reorder_strategy in ALL_STRATEGY_COMBINATIONS:
        # Skip large length strategies
        if length_strategy in [LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE, LengthStrategy.LARGEST_POSSIBLE]:
            continue
            
        test_cases = generate_test_cases(
            target_strategy=target_strategy,
            golden_strategy=golden_strategy,
            length_strategy=length_strategy,
            reorder_strategy=reorder_strategy
        )
        all_test_cases.extend(test_cases)
    
    return all_test_cases


def strategy_to_description(target_strategy: TargetStrategy, golden_strategy: GoldenNumberStrategy, 
                          length_strategy: LengthStrategy, dull_strategy: DullNumberStrategy, 
                          reorder_strategy: ReorderStrategy) -> str:
    """Convert strategy enum values to human-readable description."""
    
    # Target strategy descriptions
    target_desc = {
        TargetStrategy.MIN_NUMBER: "min target",
        TargetStrategy.MIN_NUMBER_PLUS_ONE: "min+1 target", 
        TargetStrategy.MAX_NUMBER: "max target",
        TargetStrategy.MAX_NUMBER_MINUS_ONE: "max-1 target",
        TargetStrategy.ZERO: "zero target",
        TargetStrategy.ONE: "one target",
        TargetStrategy.NEGATIVE_ONE: "negative one target",
        TargetStrategy.RANDOM_NEGATIVE: "random negative target",
        TargetStrategy.RANDOM_POSITIVE: "random positive target"
    }
    
    # Golden strategy descriptions
    golden_desc = {
        GoldenNumberStrategy.CLOSEST: "closest pair",
        GoldenNumberStrategy.MOST_DISTANT: "most distant pair",
        GoldenNumberStrategy.RANDOM: "random pair"
    }
    
    # Length strategy descriptions
    length_desc = {
        LengthStrategy.LEAST_POSSIBLE: "min length",
        LengthStrategy.LARGEST_POSSIBLE: "max length",
        LengthStrategy.LEAST_POSSIBLE_PLUS_ONE: "min+1 length",
        LengthStrategy.LARGEST_POSSIBLE_MINUS_ONE: "max-1 length",
        LengthStrategy.SOMEWHAT_LARGE: "large length",
        LengthStrategy.SOMEWHAT_SMALL: "small length"
    }
    
    # Dull strategy descriptions
    dull_desc = {
        DullNumberStrategy.RANGE1_ONLY: "range1 only",
        DullNumberStrategy.RANGE2_ONLY: "range2 only", 
        DullNumberStrategy.RANGE3_ONLY: "range3 only",
        DullNumberStrategy.RANGE1_AND_2: "range1+2",
        DullNumberStrategy.RANGE1_AND_3: "range1+3",
        DullNumberStrategy.RANGE2_AND_3: "range2+3",
        DullNumberStrategy.ALL_RANGES: "all ranges"
    }
    
    # Reorder strategy descriptions
    reorder_desc = {
        ReorderStrategy.ASC_ORDERED: "ascending",
        ReorderStrategy.DESC_ORDERED: "descending", 
        ReorderStrategy.RANDOMLY_SHUFFLED: "shuffled"
    }
    
    parts = [
        target_desc[target_strategy],
        golden_desc[golden_strategy], 
        length_desc[length_strategy],
        dull_desc[dull_strategy],
        reorder_desc[reorder_strategy]
    ]
    
    return ", ".join(parts)


if __name__ == "__main__":
    test_cases = generate_all_test_cases()
    print(f"Generated {len(test_cases)} test cases:")
    for tc in test_cases:
        print(f"ID: {tc.id}")
        print(f"  Strategies:")
        print(f"    Target: {tc.target_strategy.name}")
        print(f"    Golden: {tc.golden_strategy.name}")
        print(f"    Length: {tc.length_strategy.name}")
        print(f"    Reorder: {tc.reorder_strategy.name}")
        print(f"    Dull: {tc.dull_strategy.name}")
        print(f"  Target: {tc.target}")
        print(f"  Nums: {tc.nums}")
        print(f"  Expected: {tc.expected}")
        print()
    
    # Save test cases to YAML file in testgen_output folder
    output_dir = "testgen_output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    yaml_filename = f"testcases_{timestamp}.yaml"
    yaml_filepath = os.path.join(output_dir, yaml_filename)
    
    # Prepare test cases for YAML output
    yaml_test_cases = []
    for tc in test_cases:
        yaml_case = {
            "id": tc.id,
            "description": strategy_to_description(
                tc.target_strategy, tc.golden_strategy, tc.length_strategy, 
                tc.dull_strategy, tc.reorder_strategy
            ),
            "input": {
                "nums": tc.nums,
                "target": tc.target
            },
            "expected": tc.expected
        }
        yaml_test_cases.append(yaml_case)
    
    # Create the YAML structure with test_cases wrapper
    yaml_data = {"test_cases": yaml_test_cases}
    
    # Write to YAML file
    with open(yaml_filepath, 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file, default_flow_style=False, sort_keys=False)
    
    print(f"\nTest cases saved to: {yaml_filepath}")