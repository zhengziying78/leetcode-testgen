"""
Two Sum solution implementation.

Source: https://leetcode.com/problems/two-sum/solutions/6754748/video-step-by-step-easy-solution/
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i
