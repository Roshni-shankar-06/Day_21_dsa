class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n
        
        for r, c in indices:
            row_count[r] += 1
     
        
