class Solution:

  def hasValidPath(self, grid: list[list[str]]) -> bool:
    m, n = len(grid), len(grid[0])

    # If the total length is odd, a balanced parentheses string is impossible
    if (m + n - 1) % 2 != 0:
      return False

    memo = {}

    def dfs(r: int, c: int, balance: int) -> bool:
      # Update balance based on current cell
      if grid[r][c] == '(':
        balance += 1
      else:
        balance -= 1

      # Prune if closing brackets exceed opening brackets
      if balance < 0:
     
