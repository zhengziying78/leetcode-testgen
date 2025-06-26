"""
ZigZag Conversion solution implementation.

Source: https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert string to zigzag pattern and read line by line.
        
        Args:
            s: Input string
            numRows: Number of rows in the zigzag pattern
            
        Returns:
            str: String read line by line from zigzag pattern
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            # Change direction when we reach top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to next row
            current_row += 1 if going_down else -1
        
        return ''.join(rows)