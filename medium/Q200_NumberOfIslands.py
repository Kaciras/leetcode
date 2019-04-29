class Solution:
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		count = 0

		def fill(x, y):
			queue = [(x, y)]
			while queue:
				x, y = queue.pop()
				grid[x][y] = ""

				if x > 0 and grid[x - 1][y] == "1":
					queue.append((x-1, y))
				if y > 0 and grid[x][y - 1] == "1":
					queue.append((x , y- 1))
				if x < len(grid) - 1 and grid[x + 1][y] == "1":
					queue.append((x + 1, y))
				if y < len(grid[0]) - 1 and grid[x][y + 1] == "1":
					queue.append((x, y + 1))

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == "1":
					fill(i, j)
					count += 1

		return count


if __name__ == '__main__':
	print(Solution().numIslands([])) # 0
	print(Solution().numIslands(
		[["1", "1", "1", "1", "0"],
		 ["1", "1", "0", "1", "0"],
		 ["1", "1", "0", "0", "0"],
		 ["0", "0", "0", "0", "0"]])) # 1
	print(Solution().numIslands(
		[["1", "1", "0", "0", "0"],
		 ["1", "1", "0", "0", "0"],
		 ["0", "0", "1", "0", "0"],
		 ["0", "0", "0", "1", "1"]])) # 3
	print(Solution().numIslands(
		[["1", "1", "1"],
		 ["0", "1", "0"],
		 ["1", "1", "1"]])) # 1
	print(Solution().numIslands(
		[["1", "0", "1"],
		 ["1", "1", "1"],
		 ["1", "0", "1"]])) # 1
