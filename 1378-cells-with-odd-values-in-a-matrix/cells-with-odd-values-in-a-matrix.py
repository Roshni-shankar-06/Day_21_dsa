class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n
        
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
            
        odd_rows = sum(1 for r in row_count if r % 2 != 0)
        odd_cols = sum(1 for c in col_count if c % 2 != 0)
        
        return odd_rows * (n - odd_cols) + odd_cols * (m - odd_rows)
