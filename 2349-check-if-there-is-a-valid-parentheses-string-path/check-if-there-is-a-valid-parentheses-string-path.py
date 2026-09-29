class Solution:

  def hasValidPath(self, grid: list[list[str]]) -> bool:
    m, n = len(grid), len(grid[0])

    # If the total length is odd, a balanced parentheses string is impossible
    if (m + n - 1) % 2 != 0:
      return False
