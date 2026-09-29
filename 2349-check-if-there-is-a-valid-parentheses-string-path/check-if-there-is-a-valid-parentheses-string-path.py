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
        return False

      # Base case: bottom-right corner
      if r == m - 1 and c == n - 1:
        return balance == 0

      if (r, c, balance) in memo:
        return memo[(r, c, balance)]

      # Move down or right
      res = False
      if r + 1 < m:
        res = res or dfs(r + 1, c, balance)
      if c + 1 < n:
        res = res or dfs(r, c + 1, balance)

      memo[(r, c, balance)] = res
      return res

    return dfs(0, 0, 0)
