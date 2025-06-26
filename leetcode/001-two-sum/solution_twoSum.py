"""
Two Sum solution implementation.

Source: https://leetcode.com/problems/two-sum/solutions/6882535/try-this-code-and-beat-100-everyone/
"""


class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        
        Args:
            nums: List[int] - array of integers
            target: int - target sum
            
        Returns:
            List[int] - indices of the two numbers that add up to target
        """
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []  # No solution found